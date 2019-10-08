from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
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


class UpdateView(TemplateView):
    model = None
    form_class = None
    template_name = None
    redirect_url = None
    object = None
    context_key = 'object'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=self.object)
        return render(request, self.template_name, context={'form': form, self.context_key: self.object})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})


class DeleteView(TemplateView):
    model = None
    template_name = None
    redirect_url = None
    object = None
    context_key = 'object'

    def get_redirect_url(self):
        return self.redirect_url

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, context={self.context_key: self.object})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        self.object.delete()
        return redirect(self.redirect_url)
