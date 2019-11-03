from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import GitHubRepo, Team


class ProfileInline(admin.StackedInline):
    model = GitHubRepo
    fields = ['avatar', 'description', 'repo_url']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

class TeamAdmin(admin.ModelAdmin):
    fields = ['user', 'project','starting_date','end_date']
    list_display = ['user', 'project','starting_date','end_date']
    list_filter = ['project']


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Team, TeamAdmin)