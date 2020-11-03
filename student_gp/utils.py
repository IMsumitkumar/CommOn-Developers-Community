import json
import datetime
from .models import MessageModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_recent_messages(request):


    messages = MessageModel.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(messages, 30)

    try:
        selected = paginator.page(page)
    except PageNotAnInteger:
        selected = paginator.page(1)
    except EmptyPage:
        selected = []

    messages_array = []

    for i in messages:
        print(i.room)
        print(i.user.username)
        print(i.message)
        print(i.date_created.strftime("%d %b %Y %H:%M %p"))


    for msg in messages:
        dict = {}
        dict['user'] = msg.user.username
        dict['message'] = msg.message
        dict['room'] = msg.room.id
        dict['datetime'] = msg.date_created.strftime("%d %b %Y %H:%M %p")
        messages_array.append(dict)

    chat_data = []
    for msg in messages_array:
        if msg["room"]  == request.user.groups.values_list('id', flat=True).first():
            dict={}
            dict['user'] = msg['user']
            dict['message'] = msg['message']
            dict['datetime'] = msg['datetime']
            chat_data.append(dict)

    return chat_data
