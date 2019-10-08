from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import TypeForm
from webapp.models import Type as Type
from webapp.views.baseclass import UpdateView, DeleteView


class TypeAddView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'type_templates/type_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditTypeView(UpdateView):
    model = Type
    template_name = 'type_templates/type_edit.html'
    redirect_url = '/'
    form_class = TypeForm
    context_key = 'type'

    def get_redirect_url(self):
        return reverse('main_page')


class DeleteTypeView(DeleteView):
    model = Type
    template_name = 'type_templates/type_delete.html'
    context_key = 'type'
    redirect_url = '/'
