from django.urls import path

from webapp.views import TaskView, CreateTaskView, EditTaskView, IndexView, DeleteTaskView, StatusAddView, \
    EditStatusView, DeleteStatusView, TypeAddView, EditTypeView, DeleteTypeView, ProjectsView, ProjectView, \
    ProjectCreateView, ProjectEditView, ProjectDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='main_page'),
    path('task/<int:pk>/', TaskView.as_view(), name='view task'),
    path('project/<int:pk>/task/create/', CreateTaskView.as_view(), name='create task'),
    path('task/<int:pk>/edit/', EditTaskView.as_view(), name='edit task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete task'),

    path('status/add/', StatusAddView.as_view(), name='add status'),
    path('status/<int:pk>/edit/', EditStatusView.as_view(), name='edit status'),
    path('status/<int:pk>/delete/', DeleteStatusView.as_view(), name='delete status'),

    path('types/add/', TypeAddView.as_view(), name='add type'),
    path('types/<int:pk>/edit/', EditTypeView.as_view(), name='edit type'),
    path('types/<int:pk>/delete/', DeleteTypeView.as_view(), name='delete type'),

    path('projects/', ProjectsView.as_view(), name='view projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='view project'),
    path('project/create/', ProjectCreateView.as_view(), name='create project'),
    path('project/<int:pk>/edit/', ProjectEditView.as_view(), name='edit project'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete project'),
]

app_name='webapp'