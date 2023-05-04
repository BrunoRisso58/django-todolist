from django.contrib import admin
from .models import TaskModel

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')

admin.site.register(TaskModel, TaskAdmin)