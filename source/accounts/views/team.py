from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView

from accounts.forms import TeamAddForm
from accounts.models import Team
from webapp.models import Project


class TeamAddView(PermissionRequiredMixin, CreateView):
    model = Team
    form_class = TeamAddForm
    template_name = 'team_add.html'
    context_object_name = 'form'
    permission_required = 'accounts.add_team'
    permission_denied_message = 'Только капитан и менеджеры проектов могут кого-то нанять!'

    def get_form_kwargs(self):
        kwargs=super(TeamAddView, self).get_form_kwargs()
        kwargs.update({'project': self.get_project()})
        return kwargs

    def form_valid(self, form):
        self.project = self.get_project()
        self.object = self.project.team.create(**form.cleaned_data)
        self.object.save()
        return redirect('webapp:view project', pk = self.project.pk)

    def get_project(self):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        return project


class TeamRemoveView(PermissionRequiredMixin, DeleteView):
    model = Team
    template_name = 'team_remove.html'
    context_object_name = 'team_member'
    permission_required = 'accounts.delete_team'
    permission_denied_message = 'Только капитан и менеджеры проектов могут кого-то уволить!'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            raise Http404('Пользователь не может удалить себя из команды!')
        self.object.end_date = datetime.now()
        self.object.save()
        return redirect('webapp:view project', self.object.project.pk)