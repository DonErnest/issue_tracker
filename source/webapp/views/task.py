from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import TaskForm
from webapp.models import Task
from webapp.views.baseclass import DetailView, UpdateView, DeleteView


class TaskView(DetailView):

    template_name = 'task_templates/task.html'
    model = Task
    context_key = 'task'


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_templates/task_create.html'
    context_key = 'task'

    def get_success_url(self):
        return reverse('view task', kwargs={'pk': self.object.pk})


class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_templates/task_edit.html'
    context_key = 'task'

    def get_redirect_url(self):
        return reverse('view task', kwargs={'pk': self.object.pk})


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task_templates/task_delete.html'
    context_key = 'task'
    redirect_url = '/'
