from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import UserSignUpForm, UserUpdateForm, UserPasswordChangeForm


def login_view(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_path = request.GET.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if redirect_path:
                return redirect(redirect_path)
            return redirect('webapp:main_page')
        else:
            context['has_error']=True
            context['next']=redirect_path
            context['username']=username

    else:
        context={'next': request.GET.get('next')}
    return render(request, 'login.html', context=context)


class UserLogoutView(LogoutView):
    next_page = 'webapp:main_page'


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('webapp:main_page')
    else:
        form=UserSignUpForm()
    return render(request, 'register.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model=User
    template_name = 'user_update.html'
    form_class = UserUpdateForm
    context_object_name = 'user_obj'



    def get_success_url(self):
        return reverse('accounts:user details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = UserPasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:login')