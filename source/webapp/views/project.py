from django.views.generic import ListView, DetailView

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
