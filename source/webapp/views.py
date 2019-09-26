from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class TaskView(TemplateView):

    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=pk)
        return context


class CreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_create.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(summary=form.cleaned_data['summary'],
                                          description=form.cleaned_data['description'],
                                          status=form.cleaned_data['status'],
                                          type=form.cleaned_data['type'])
            return redirect('view task', pk=task.pk)
        return render(request, 'task_create.html', context={'form':form})

class EditView(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={'summary': task.summary,
                              'description': task.description,
                              'status': task.status_id,
                              'type': task.type_id})
        return render(request, 'task_edit.html', context={'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('view task', pk=task.pk)
        else:
            return render(request, 'task_edit.html', context={
                'form': form, 'task': task
            })