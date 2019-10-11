from django.contrib import admin

from webapp.models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type','created_at', 'project']
    list_display_links = ['id', 'summary']
    list_filter = ['type', 'status']
    search_fields = ['summary', 'description', 'project']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'project']
    readonly_fields = ['created_at']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    fields= ['name','description', 'status', 'created_at','updated_at']
    readonly_fields = ['created_at','updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)
