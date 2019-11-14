from django import forms
from django.contrib.auth.models import User

from webapp.models import Status, Type, Task, Project


class TaskCreateForm(forms.ModelForm):
    def __init__(self, project, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'] = forms.ModelChoiceField(queryset=User.objects.filter(team__project=project))

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'assigned_to']
        labels = {'summary': 'Краткое описание', 'description': 'Подробно', 'status': 'Статус', 'type': 'Тип', 'assigned_to': 'Исполнитель'}



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


class ProjectCreateForm(forms.ModelForm):
    starting_date = forms.DateField(label='Дата начала работы в проекте')
    project_squad = forms.ModelMultipleChoiceField(queryset=User.objects.all())


    def save(self, commit=True):
        project = super(ProjectCreateForm, self).save(commit)
        return project

    class Meta:
        model = Project
        fields=['name', 'description', 'status', 'project_squad', 'starting_date']
        team_fields = ['project_squad', 'starting_date']
        labels = {'name': 'Название проекта', 'description': 'Описание проекта', 'squad': 'Команда'}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['name', 'description', 'status']
        labels = {'name': 'Название проекта', 'description': 'Описание проекта'}

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

class AddUserToProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['squad']
        labels = {'squad': 'Команда'}
