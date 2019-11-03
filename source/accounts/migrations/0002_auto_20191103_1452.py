# Generated by Django 2.2 on 2019-11-03 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='githubrepo',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='githubrepo',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='githubrepo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
