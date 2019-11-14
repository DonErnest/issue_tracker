# Generated by Django 2.2 on 2019-11-12 16:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_team'),
        ('webapp', '0007_auto_20191106_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='squad',
            field=models.ManyToManyField(blank=True, related_name='projects', through='accounts.Team', to=settings.AUTH_USER_MODEL),
        ),
    ]