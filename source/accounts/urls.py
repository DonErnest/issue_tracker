from django.urls import path
from accounts.views import UserLogoutView, login_view, register_view, UserDetailView, UserUpdateView, \
    UserPasswordChangeView, UserListView

urlpatterns = [
    path('login/', login_view, name='login' ),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='user details'),
    path('<int:pk>/edit', UserUpdateView.as_view(), name='update user info'),
    path('<int:pk>/password', UserPasswordChangeView.as_view(), name='change user password'),
    path('users/', UserListView.as_view(), name='list users')
]


app_name='accounts'