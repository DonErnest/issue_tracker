from django.urls import path
from accounts.views import UserLogoutView, login_view

urlpatterns = [
    path('login/', login_view, name='login' ),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]


app_name='accounts'