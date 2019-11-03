from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task, PROJECT_STATUS_DEFAULT, Project


class TaskView(DetailView):
    template_name = 'task_templates/task.html'
    model = Task
    context_key = 'task'


class CreateTaskView(UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_templates/task_create.html'
    context_key = 'task'

    def get_success_url(self):
        return reverse('webapp:view task', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super(CreateTaskView, self).get_form()
        form.fields['project'].queryset = Project.objects.filter(team__user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            selected_project = form.cleaned_data['project']
            if selected_project.status == PROJECT_STATUS_DEFAULT:
                return self.form_valid(form)
            else:
                raise Http404('Невозможно создать задачу для закрытого проекта!')
        else:
            return self.form_invalid(form)

    def test_func(self):
        return True



class EditTaskView(UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_templates/task_edit.html'
    context_key = 'task'

    def get_success_url(self):
        return reverse('webapp:view task', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            selected_project = form.cleaned_data['project']
            if selected_project.status == PROJECT_STATUS_DEFAULT:
                return self.form_valid(form)
            else:
                raise Http404('Невозможно реадктировать задачу для закрытого проекта!')
        else:
            return self.form_invalid(form)

    def test_func(self):
        teams = self.request.user.team.distinct()
        pk = self.kwargs['pk']
        task = Task.objects.get(pk=pk)
        return teams.filter(project=task.project)

class DeleteTaskView(UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'task_templates/task_delete.html'
    context_key = 'task'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # print(self.object.project.status)
        if self.object.project.status == PROJECT_STATUS_DEFAULT:
            return self.delete(request, *args, **kwargs)
        else:
            raise Http404('Невозможно удалить задачу для закрытого проекта!')

    def test_func(self):
        teams = self.request.user.team.distinct()
        pk = self.kwargs['pk']
        task = Task.objects.get(pk=pk)
        return teams.filter(project=task.project)