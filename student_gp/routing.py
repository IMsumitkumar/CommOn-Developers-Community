from django.urls import re_path

from . import consumers as a
from user_group import consumers as b

websocket_urlpatterns = [
    re_path(r'ws/student_gp/(?P<room_name>\w+)/$', a.ChatConsumer.as_asgi()),
    re_path(r'ws/ug_api/(?P<room_name>[^/]+)/$', b.ChatConsumer.as_asgi()),
]
