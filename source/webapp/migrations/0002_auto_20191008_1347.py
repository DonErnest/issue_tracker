# Generated by Django 2.2 on 2019-10-08 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='project_name')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='project_description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='project_created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='project_updated')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='webapp.Project', verbose_name='projects'),
        ),
    ]
