from django.views.generic import TemplateView, ListView

from webapp.models import Task, Status, Type as Type


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 6
    paginate_orphans = 1


    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['status']= Status.objects.all()
        context['types']= Type.objects.all()
        return context
