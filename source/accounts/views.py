from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.forms import UserSignUpForm, UserUpdateForm, UserPasswordChangeForm
from accounts.models import GitHubRepo


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     try:
    #         git_repo_form = GitURLForm(initial={'user': self.object, 'repo_url': self.object.githubrepo})
    #         context['git_repo'] = git_repo_form
    #     except:
    #         git_repo_form = GitURLForm()
    #         context['git_repo'] = git_repo_form
    #     return context


    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     user_pk = self.kwargs['pk']
    #     user = get_object_or_404(User, pk=user_pk)
    #     repo_url = request.POST['repo_url']
    #     git_obj = GitHubRepo(user=user, repo_url=repo_url)
    #     form = self.get_form()
    #     print(form)
    #     if form.is_valid():
    #         git_obj.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


    def get_success_url(self):
        return reverse('accounts:user details', kwargs={'pk': self.kwargs['pk']})

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


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

