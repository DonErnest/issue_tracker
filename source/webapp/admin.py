from django.contrib import admin

from webapp.models import Task, Type, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type','created_at']
    list_display_links = ['id', 'summary']
    list_filter = ['type', 'status']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)

