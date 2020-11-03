import json
import os
import pickle
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import MessageModel
from .meta_matcher import string_match
from .toxic_comment import toxic_classifier
import markdown


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.room_id = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_id

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.user
        room_id = self.room_id
        room = await self.get_group_instance(room_id)

        # time = await self.save_message_to_db(room, user, message)

        msg = markdown.markdown(str(message))

        toxic = await toxic_classifier(message)
        meta_pattern_type,_ = await string_match(message)


        if toxic[0] >= 90:
            time = None
        else:
            time = await self.save_message_to_db(room, user, message)
            time = time.strftime("%d %b %Y %H:%M:%S %Z")

        # print(message)
        # print(toxic[0])
        print(time)
        # print(meta_pattern_type)
        # now = timezone.now()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg,
                'user':self.user.username,
                'datetime': time,
                'toxic': toxic,
                'is_meta':meta_pattern_type,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_message(self, event):
        await self.send(text_data=json.dumps(event))



    @database_sync_to_async
    def save_message_to_db(self, groupname, username, message):
        toxic = toxic_classifier(message)

        new_message = MessageModel(room=groupname, user=username, message=message)
        new_message.save()
        new_message.recipients.add(username)
        new_message.save()
        groupname.date_modified = new_message.date_modified
        groupname.save()
        return new_message.date_created



    @sync_to_async
    def get_user_instance(self, name):
        return User.objects.get(username=name)

    @sync_to_async
    def get_group_instance(request, room_id):
        # return self.user.groups.values_list('name', flat=True).first()
        return request.user.groups.get(id=room_id)
