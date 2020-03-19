from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    users = models.ManyToManyField(to=User, related_name='projects')

    def __str__(self):
        return self.title
