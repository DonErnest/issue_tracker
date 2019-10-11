from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project, PROJECT_STATUS_DEFAULT


class ProjectsView(ListView):
    template_name = 'project_templates/project_list.html'
    model = Project
    # context_object_name = 'projects'
    paginate_by = 6
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_active'] = self.model.objects.filter(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
        context['projects_closed'] = self.model.objects.exclude(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
        return context


class ProjectView(DetailView):
    template_name = 'project_templates/project.html'
    model = Project
    context_key = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['tasks'] = self.object.tasks.filter(project_id = project.pk)
        return context



class ProjectCreateView(CreateView):
    template_name = 'project_templates/project_create.html'
    model = Project
    context_object_name = 'form'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('view project', kwargs={'pk':self.object.pk})


class ProjectEditView(UpdateView):
    template_name = 'project_templates/project_update.html'
    model = Project
    context_object_name = 'project'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('view project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project_templates/project_delete.html'
    model = Project
    form_class = ProjectForm
    success_url = '/projects/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)


