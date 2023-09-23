import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import User
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Handle WebSocket connection initiation
        pass

    async def disconnect(self, close_code):
        # Handle WebSocket disconnection
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')
        recipient_username = data.get('recipient_username', '')

        # Validate recipient's online status
        try:
            recipient = User.objects.get(username=recipient_username)
            recipient_profile = UserProfile.objects.get(user=recipient)
            if recipient_profile.online:
                # Recipient is online, send the message
                await self.send_message(message, recipient_username)
            else:
                # Recipient is offline, handle accordingly (e.g., notify the sender)
                await self.handle_offline_recipient(recipient_username)
        except User.DoesNotExist:
            # Handle recipient not found
            pass

    async def send_message(self, message, recipient_username):
        # Send the message to the recipient's WebSocket
        pass

    async def handle_offline_recipient(self, recipient_username):
        # Handle the case where the recipient is offline (e.g., notify the sender)
        pass
