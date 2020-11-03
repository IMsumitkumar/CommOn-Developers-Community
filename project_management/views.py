from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Project
from django.db.models import Avg
from django.db.models import Q
from .forms import ProjectForm, TaskForm
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page


def index(request):
    projects = Project.objects.filter(admin=request.user)[:1]
    for project in projects:
        tasks = Task.objects.filter(project=project.id)
        project_name = Project.objects.get(id = project.id)
        if request.method == 'POST':
            task_form = TaskForm(request.POST, request.FILES)
            if task_form.is_valid():
                project = task_form.save(commit=False)
                project.project = project_name
                project.save()
                return redirect('/myproject/')
        else:
            task_form = TaskForm()

    context = {'tasks':tasks, 'task_form':task_form}
    return render(request, 'project_management/project_index.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.admin = request.user
            instance.save()
            return redirect('/')
    else:
        form = ProjectForm()

    context = {'form':form}
    return render(request, 'project_management/project_add.html', context)



def add_user(request):
    if request.method =='POST':
        recipient_username=request.POST.get('firstname')
        recipient = User.objects.get(username=str(recipient_username))
        projects = Project.objects.filter(admin=request.user)
        for project in projects:
            project.recipients.add(recipient)
        return redirect('/myproject/')

def UpdateTask(request, pk):

    task = Task.objects.get(id=pk)
    updatetask_form = TaskForm(instance=task)

    if request.method =='POST':
        updatetask_form = TaskForm(request.POST, instance=task)
        if updatetask_form.is_valid():
            updatetask_form.save()
            return redirect('/myproject/')

    context = {'updatetask_form':updatetask_form}

    return render(request, 'project_management/update_task.html', context)


def DeleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/myproject/')


    context = {'task_item':task}
    return render(request, 'project_management/delete_task.html', context)