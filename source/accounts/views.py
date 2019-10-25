import urllib
from urllib.parse import urlencode

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def login_view(request, *args, **kwargs):
    context={}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_path = request.GET.get('next')
            if redirect_path == 'None' or redirect_path=='':
                redirect_path = 'webapp:main_page'
            return redirect(redirect_path)
        else:
            context['has_error']=True
    return render(request, 'login.html', context=context)


class UserLogoutView(LogoutView):
    next_page = 'webapp:main_page'


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', context={'form':form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('webapp:main_page')
        else:
            return render(request, 'register.html', context={'form': form})