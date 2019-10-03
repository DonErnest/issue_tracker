from django.db.models import ProtectedError
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import StatusForm
from webapp.models import Status



class StatusAddView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status_templates/status_add.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class EditStatusView(UpdateView):
    model = Status
    fields = ['name']
    template_name = 'status_templates/status_edit.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteStatusView(DeleteView):
    model = Status
    template_name = 'status_templates/status_delete.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'protected_error.html')