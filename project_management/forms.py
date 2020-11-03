from .models import Project, Task
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'complete_per', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due', 'body']
