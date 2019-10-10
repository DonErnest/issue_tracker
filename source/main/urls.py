from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, TaskView, CreateTaskView, EditTaskView, DeleteTaskView, StatusAddView, TypeAddView, \
    EditStatusView, DeleteStatusView, EditTypeView, DeleteTypeView, ProjectsView, ProjectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='main_page'),
    path('task/<int:pk>/', TaskView.as_view(), name='view task'),
    path('task/create/', CreateTaskView.as_view(), name='create task'),
    path('task/<int:pk>/edit/', EditTaskView.as_view(), name='edit task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete task'),
    path('status/add/', StatusAddView.as_view(), name='add status'),
    path('status/<int:pk>/edit', EditStatusView.as_view(), name='edit status'),
    path('status/<int:pk>/delete', DeleteStatusView.as_view(), name='delete status'),
    path('types/add/', TypeAddView.as_view(), name='add type'),
    path('types/<int:pk>/edit', EditTypeView.as_view(), name='edit type'),
    path('types/<int:pk>/delete', DeleteTypeView.as_view(), name='delete type'),
]
