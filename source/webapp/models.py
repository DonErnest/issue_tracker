from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='summary')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='description')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT,related_name='tasks', verbose_name='status')
    type = models.ForeignKey('webapp.Type',on_delete=models.PROTECT, related_name='tasks', verbose_name='type')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='created')

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
