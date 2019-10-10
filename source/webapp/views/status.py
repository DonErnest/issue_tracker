from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import StatusForm
from webapp.models import Status
from webapp.views.baseclass import UpdateView, DeleteView


class StatusAddView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_templates/status_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditStatusView(UpdateView):
    model = Status
    template_name = 'status_templates/status_edit.html'
    form_class = StatusForm
    context_key = 'status'
    def get_redirect_url(self):
        return reverse('main_page')


class DeleteStatusView(DeleteView):
    model = Status
    template_name = 'status_templates/status_delete.html'
    context_key = 'status'
    redirect_url = '/'
    confirmation = False