from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
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
        text_data_dict = json.loads(text_data)
        message = text_data_dict['message']

        print('in ClientConsumer.receive, receive a message:' + message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, text_data_dict)

    # Receive message from room group
    async def client_message(self, event):
        message = event['message']

        print('in ClientConsumers.client_message, receive a client_message:' + message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Receive message from room group
    async def service_message(self, event):
        message = event['message']

        print('in ClientConsumers.Service_message, receive a Service_message:' + message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

class ServiceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
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
        text_data_dict = json.loads(text_data)
        message = text_data_dict['message']

        print('in ServiceConsumer.receive, receive a message:' + message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, text_data_dict)

    # Receive message from room group
    async def client_message(self, event):
        message = event['message']

        print('in ServiceConsumers.client_message, receive a client_message:' + message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    # Receive message from room group
    async def service_message(self, event):
        message = event['message']

        print('in ServiceConsumers.Service_message, receive a service_message:' + message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))