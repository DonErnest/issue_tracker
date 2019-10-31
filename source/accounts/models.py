from django.contrib.auth.models import User
from django.db import models

class GitHubRepo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    repo_url = models.URLField(verbose_name='github repo url')

    def __str__(self):
        return self.repo_url