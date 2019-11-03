from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import GitHubRepo


class ProfileInline(admin.StackedInline):
    model = GitHubRepo
    fields = ['avatar', 'description', 'repo_url']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)