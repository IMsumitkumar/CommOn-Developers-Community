from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupSerializer
from django.contrib.auth.models import User
from .forms import UserGroupForm
from .models import CreateGroup
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)


# --------------------------------------------------------------------------

@api_view(['GET'])
def groupList(request):
    tasks = CreateGroup.objects.all().order_by('id')
    serializer = GroupSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GroupList(request):
    tasks = CreateGroup.objects.all().order_by('id')
    serializer = GroupSerializer(tasks, many=True)
    context = {'groups':serializer.data}
    return render(request, 'user_group/user_group.html', context)

# --------------------------------------------------------------------------

@api_view(['GET'])
def groupDetail(request, pk):
    tasks = CreateGroup.objects.get(id=pk)
    serializer = GroupSerializer(tasks, many=False)
    data = serializer.data
    group_name = data['group_name']
    print(group_name)
    return Response(serializer.data)

# --------------------------------------------------------------------------

@api_view(['POST'])
def groupCreate(request):
    serializer = GroupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def groupUpdate(request, pk):
    task = CreateGroup.objects.get(id=pk)
    serializer = GroupSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def groupDelete(request, pk):
    task = CreateGroup.objects.get(id=pk)
    task.delete()

    return Response("Item successfully Deleted!")


# -----------------------------------------------------------------------------

@login_required(login_url='login')
def group_create(request):

    if request.method == 'POST':
        gc_form = UserGroupForm(request.POST, request.FILES)
        if gc_form.is_valid():
            instance = gc_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/ug_api/groups/')
    else:
        gc_form = UserGroupForm()
    
    groups = CreateGroup.objects.filter(user=request.user)
    
    context = {'gc_form':gc_form, 'my_group':groups}
    return render(request, 'user_group/create_group.html', context)




def room(request, room_name):

    return render(request, 'user_group/user_room.html', {
        'room_name': room_name
    })