from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)