from django.db.models import ProtectedError
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import TypeForm
from webapp.models import Type as Type


class TypeAddView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'type_templates/type_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditTypeView(UpdateView):
    model = Type
    fields = ['name']
    template_name = 'type_templates/type_edit.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteTypeView(DeleteView):
    model = Type
    template_name = 'type_templates/type_delete.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'protected_error.html')