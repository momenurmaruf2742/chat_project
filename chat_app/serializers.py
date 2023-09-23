from rest_framework import serializers
from .models import User, Message,Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'online')  # Include desired fields

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all_'