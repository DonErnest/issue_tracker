from django.contrib.auth.models import User
from django.db import models

class GitHubRepo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    avatar = models.ImageField(null=True, blank=True,  verbose_name='Аватар', upload_to='user_pics')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='О себе')
    repo_url = models.URLField(verbose_name='github repo url')

    def __str__(self):
        return self.user.get_full_name() + "'s profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


