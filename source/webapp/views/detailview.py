from django.http import Http404
from django.views.generic import TemplateView


class DetailView(TemplateView):
    context_key = 'object'
    model = None

    def get_object(self, pk):
        try:
            some_object = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404('НЕТ ТАКОГО ОБЪЕКТА!')
        return some_object

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_object(pk=pk)
        return context
