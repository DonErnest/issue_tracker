import urllib
from urllib.parse import urlencode

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request, *args, **kwargs):
    context={}
    if request.method == 'GET':
        redirect_url = request.GET.get('next')
        context['redirect_url'] = redirect_url
        return render(request, 'login.html', context=context)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_path = request.POST.get('redirect_url')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if redirect_path == 'None' or redirect_path=='':
                redirect_path = 'webapp:main_page'
            return redirect(redirect_path)
        else:
            context['has_error']=True
    return render(request, 'login.html', context=context)


class UserLogoutView(LogoutView):
    next_page = 'webapp:main_page'
