from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import login_view, UserLogoutView
from main import settings
from webapp.views import IndexView, TaskView, CreateTaskView, EditTaskView, DeleteTaskView, StatusAddView, TypeAddView, \
    EditStatusView, DeleteStatusView, EditTypeView, DeleteTypeView, ProjectsView, ProjectView, ProjectCreateView, \
    ProjectEditView, ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/v1/', include('api_v1.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)