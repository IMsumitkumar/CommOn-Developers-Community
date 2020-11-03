from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','project']
    list_filter = ['project', ]
    search_fields = ['project']
    
admin.site.register(Task, TaskAdmin)
