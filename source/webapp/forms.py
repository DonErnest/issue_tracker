from django import forms

from webapp.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'project']
        labels = {'summary': 'Краткое описание', 'description': 'Подробно', 'status': 'Статус', 'type': 'Тип',
                  'project': 'Проект'}


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
        fields=['name', 'description', 'status']
        labels = {'name': 'Название проекта', 'description': 'Описание проекта'}

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
