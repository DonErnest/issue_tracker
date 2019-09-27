from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView

from webapp.forms import TaskForm, StatusForm, TypeForm
from webapp.models import Task, Status, Type


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['status']= Status.objects.all()
        context['types']= Type.objects.all()
        return context

class TaskView(TemplateView):

    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=pk)
        return context


class CreateTaskView(TemplateView):
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

class EditTaskView(TemplateView):
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


class DeleteTaskView(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_delete.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('main_page')


class StatusAddView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status_add.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(name=form.cleaned_data['status'])
            return redirect('main_page')
        return render(request, 'status_add.html', context={'form': form})

class EditStatusView(CreateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={'status': status.name})
        return render(request, 'status_edit.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['status']
            status.save()
            return redirect('main_page')
        else:
            return render(request, 'status_edit.html', context={
                'form': form, 'status': status
            })

class DeleteStatusView(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status_delete.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('main_page')


class TypeAddView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type_add.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(name=form.cleaned_data['type'])
            return redirect('main_page')
        return render(request, 'type_add.html', context={'form': form})


class EditTypeView(CreateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task_type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={'type': task_type.name})
        return render(request, 'type_edit.html', context={'form': form, 'type': task_type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['type']
            type.save()
            return redirect('main_page')
        else:
            return render(request, 'type_edit.html', context={
                'form': form, 'type': type
            })

class DeleteTypeView(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=pk)
        type.delete()
        return redirect('main_page')