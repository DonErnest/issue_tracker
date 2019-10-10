from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'project_templates/project_list.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 6
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'project_templates/project.html'
    model = Project
    context_key = 'project'


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
