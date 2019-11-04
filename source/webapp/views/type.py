from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import TypeForm
from webapp.models import Type as Type


class TypeAddView(LoginRequiredMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'type_templates/type_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditTypeView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type_templates/type_edit.html'
    success_url = '/'
    form_class = TypeForm
    context_key = 'type'


class DeleteTypeView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'type_templates/type_delete.html'
    context_key = 'type'
    success_url = '/'
