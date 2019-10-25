from django.contrib import admin
from django.urls import path, include

from accounts.views import login_view, UserLogoutView
from webapp.views import IndexView, TaskView, CreateTaskView, EditTaskView, DeleteTaskView, StatusAddView, TypeAddView, \
    EditStatusView, DeleteStatusView, EditTypeView, DeleteTypeView, ProjectsView, ProjectView, ProjectCreateView, \
    ProjectEditView, ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls'))
]
