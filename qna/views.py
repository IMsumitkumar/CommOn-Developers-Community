from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from student_gp.models import MessageModel
from django.contrib.auth.models import User
from .models import Question, Answer

def QnA(request):
    questions = Question.objects.all()[:10]


    context = {
        'questions':questions,
    }
    return render(request, 'qna/QnA.html', context)


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


@api_view(['GET'])
def taskList(request):
    tasks = MessageModel.objects.all()
    end = tasks.count()
    room_id = request.user.groups.values_list('id', flat=True).first()
    room_msg = MessageModel.objects.filter(room=room_id)

    if end <=50:
        tasks = MessageModel.objects.filter(room=room_id).order_by('id')
        serializer = MessageSerializer(tasks, many=True)
        return Response(serializer.data)
    else:
        tasks = MessageModel.objects.filter(room=room_id).order_by('id')[end-50:end]
        serializer = MessageSerializer(tasks, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def SaveQuesItem(request, pk):
    tasks = MessageModel.objects.get(id=pk)
    serializer = MessageSerializer(tasks, many=False)
    dict = serializer.data
    user = dict.get("user")
    username = User.objects.get(id=user)
    message = dict.get("message")
    date_created = dict.get("date_created")

    n = Question.objects.create(ques=message, asker=username)
    # print(n.id)

    return Response(serializer.data)


@api_view(['GET'])
def SaveAnsItem(request, pk):
    tasks = MessageModel.objects.get(id=pk)
    serializer = MessageSerializer(tasks, many=False)
    dict = serializer.data
    user = dict.get("user")
    username = User.objects.get(id=user)
    message = dict.get("message")
    date_created = dict.get("date_created")

    msgs = Question.objects.filter(asker=request.user).order_by('-id')[:1]

    for msg in msgs:
        print(msg)
        Answer.objects.create(question=msg, teller=username, ans=message)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = MessageModel.objects.get(id=pk)
    serializer = MessageSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = MessageModel.objects.get(id=pk)
    task.delete()

    return Response("Item successfully Deleted!")
