from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.chat}: {self.content}'