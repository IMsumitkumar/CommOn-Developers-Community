import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
import markdown



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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

        time = timezone.now()
        datetime = time.strftime("%d %b %Y %H:%M:%S %Z")

        msg = markdown.markdown(str(message))

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg,
                'user':self.user.username,
                'datetime':datetime,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_message(self, event):
        await self.send(text_data=json.dumps(event))