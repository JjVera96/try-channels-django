# chat/routing.py
from django.conf.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/chat/(?P<room_name>[\w-]+)$', consumers.ChatConsumer),
]