from django import forms

from webapp.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'projects']
        labels = {'summary': 'Краткое описание', 'description': 'Подробно', 'status': 'Статус', 'type': 'Тип'}


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': 'Новый статус'}


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        labels = {'name': 'Новый тип'}


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['name', 'description']
        labels = {'name': 'Название проекта', 'description': 'Описание проекта'}
