from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(verbose_name='description')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

