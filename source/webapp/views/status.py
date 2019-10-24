from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import StatusForm
from webapp.models import Status


class StatusAddView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_templates/status_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status_templates/status_edit.html'
    form_class = StatusForm
    context_key = 'status'
    def get_success_url(self):
        return reverse('main_page')


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status_templates/status_delete.html'
    context_key = 'status'
    success_url = '/'