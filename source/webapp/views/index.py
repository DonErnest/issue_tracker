from django.views.generic import TemplateView

from webapp.models import Task, Status, Type as Type


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['status']= Status.objects.all()
        context['types']= Type.objects.all()
        return context
