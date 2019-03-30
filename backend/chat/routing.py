from django.conf.urls import url
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/client/<str:room_name>/', consumers.ClientConsumer),
    path('ws/service/<str:room_name>/', consumers.ServiceConsumer),
]