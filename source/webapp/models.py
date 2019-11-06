from django.contrib.auth.models import User
from django.db import models

PROJECT_STATUS_DEFAULT = 'active'
PROJECT_STATUSES=[(PROJECT_STATUS_DEFAULT, 'Активный'),('closed','Закрыт')]

class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='summary')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='description')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT,related_name='tasks', verbose_name='status',
                               null=True, blank=True)
    type = models.ForeignKey('webapp.Type',on_delete=models.PROTECT, related_name='tasks', verbose_name='type',
                             null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='tasks', verbose_name='projects', null=True, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks_created', verbose_name='author', null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned', verbose_name='executor', null=True, blank=True)


    def __str__(self):
        return self.summary


class Type(models.Model):
    name = models.CharField(max_length=15, verbose_name='task_name')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=15, verbose_name='status_name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Status'
        verbose_name_plural='Status'


class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False, verbose_name='project_name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='project_description')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='project_created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='project_updated')
    status = models.CharField(choices=PROJECT_STATUSES, max_length=10, default=PROJECT_STATUS_DEFAULT, verbose_name='Статус проекта')

    def __str__(self):
        return self.name