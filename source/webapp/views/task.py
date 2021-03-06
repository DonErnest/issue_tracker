from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import TaskForm, TaskCreateForm
from webapp.models import Task, PROJECT_STATUS_DEFAULT, Project


class TaskView(DetailView):
    template_name = 'task_templates/task.html'
    model = Task
    context_key = 'task'


class CreateTaskView(UserPassesTestMixin, PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_templates/task_create.html'
    context_key = 'task'
    permission_required = 'webapp.add_task'
    permission_denied_message = 'Ты вообще кто?!'

    def form_valid(self, form):
        self.project = self.get_project()
        self.object = self.project.tasks.create(**form.cleaned_data)
        self.object.created_by = self.request.user
        self.object.save()
        return redirect('webapp:view task', pk = self.object.pk)

    def get_project(self):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        if project.status =='closed':
            raise Http404('Невозможно создать задачу для закрытого проекта!')
        return project

    def get_success_url(self):
        return reverse('webapp:view task', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs=super(CreateTaskView, self).get_form_kwargs()
        kwargs.update({'project': self.get_project()})
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def test_func(self):
        teams = self.request.user.team.distinct()
        pk = self.kwargs['pk']
        project = Project.objects.get(pk=pk)
        return teams.filter(project=project, end_date=None)


class EditTaskView(UserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_templates/task_edit.html'
    context_key = 'task'
    permission_required = 'webapp.change_task'
    permission_denied_message = 'Ты вообще кто?!'

    def get_success_url(self):
        return reverse('webapp:view task', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({'project': self.object.project})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.project.status=='closed':
            raise Http404('Невозможно редактировать задачу для закрытого проекта!')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


    def test_func(self):
        teams = self.request.user.team.distinct()
        pk = self.kwargs['pk']
        task = Task.objects.get(pk=pk)
        return teams.filter(project=task.project, end_date=None)

class DeleteTaskView(UserPassesTestMixin, PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_templates/task_delete.html'
    context_key = 'task'
    success_url = '/'
    permission_required = 'webapp.delete_task'
    permission_denied_message = 'Ты вообще кто?!'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.project.status == PROJECT_STATUS_DEFAULT:
            return self.delete(request, *args, **kwargs)
        else:
            raise Http404('Невозможно удалить задачу для закрытого проекта!')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        teams = self.request.user.team.distinct()
        pk = self.kwargs['pk']
        task = Task.objects.get(pk=pk)
        return teams.filter(project=task.project, end_date=None)