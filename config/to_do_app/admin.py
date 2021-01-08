from django.contrib import admin
from .models import TaskModel

# Register your models here.


@admin.register(TaskModel)
class TasksModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc',
                    'completed', 'created', 'updated_time']
