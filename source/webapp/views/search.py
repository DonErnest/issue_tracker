# from urllib.parse import urlencode
#
# from django.db.models import Q
# from django.views.generic import ListView
#
# from webapp.forms import SearchForm
# from webapp.models import PROJECT_STATUS_DEFAULT
#
#
# class SearchView(ListView):
#     filter = {'field':None , 'criteria': None}
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_query(self):
#
#         return Q(exec(field__criteria = self.search.value in self.filter))
#
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.search_value:
#             query = self.get_query()
#             queryset = queryset.filter(query)
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             context['query'] = urlencode({'search': self.search_value})
#         else:
#             context['projects_active'] = self.model.objects.filter(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
#             context['projects_closed'] = self.model.objects.exclude(status=PROJECT_STATUS_DEFAULT).order_by('created_at')
#         return context
#
#     def get_search_form(self):
#         return SearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#         return None