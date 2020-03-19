from django.db import models
from projects.models import Project
from bug_reports.constants import Severity, Status


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=Severity.CHOICES, default=Severity.MEDIUM)
    status = models.CharField(max_length=20, choices=Status.CHOICES, default=Status.INPROGRESS)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bug')

    def __str__(self):
        return f'bug {self.title}'

# Create your models here.
