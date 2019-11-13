from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.forms import TeamAddForm
from accounts.models import Team
from webapp.forms import ProjectForm, SearchForm
from webapp.models import Project, PROJECT_STATUS_DEFAULT


class ProjectsView(ListView):
    template_name = 'project_templates/project_list.html'
    model = Project
    context_object_name = 'projects'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value.lower())
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        else:
            context['projects_active'] = self.model.objects.filter(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
            context['projects_closed'] = self.model.objects.exclude(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectView(DetailView):
    template_name = 'project_templates/project.html'
    model = Project
    context_key = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at')
        paginator = Paginator(tasks, 3, 1)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['tasks'] = page.object_list
        context['is_paginated'] = page.has_other_pages()
        context['team'] = User.objects.filter(team__project=project)
        context['project_squad'] = Team.objects.filter(project=project, end_date=None).distinct()
        context['form'] = TeamAddForm(project=self.object)
        return context



class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project_templates/project_create.html'
    model = Project
    context_object_name = 'form'
    form_class = ProjectForm

    def form_valid(self, form):
        self.object = form.save()
        print(form.cleaned_data['project_squad'])

        for user in form.cleaned_data['project_squad']:
            Team.objects.create(project=self.object, starting_date=form.cleaned_data['starting_date'], user=user)
        if self.request.user not in form.cleaned_data['project_squad']:
            Team.objects.create(project = self.object, starting_date=datetime.now(), user_id=self.request.user.id)

        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse('webapp:view project', kwargs={'pk':self.object.pk})


class ProjectEditView(LoginRequiredMixin, UpdateView):
    template_name = 'project_templates/project_update.html'
    model = Project
    context_object_name = 'project'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:view project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project_templates/project_delete.html'
    model = Project
    success_url = '/projects/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)


