from django import forms
from django.forms import widgets

from webapp.models import Status, Type

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label = 'Краткое описание')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    status=forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус')
    type=forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Тип')


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


