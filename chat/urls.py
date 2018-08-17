from django.urls import path, re_path

from chat import views

urlpatterns = [
    path('chat', views.index, name='index'),
    re_path('(?P<room_name>[\w-]+)/$', views.room, name='room')
]