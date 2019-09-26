from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, TaskView, CreateView, EditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='main_page'),
    path('task/<int:pk>/', TaskView.as_view(), name='view task'),
    path('task/create/', CreateView.as_view(), name='create task'),
    path('task/<int:pk>/edit/', EditView.as_view(), name='edit task')
]
