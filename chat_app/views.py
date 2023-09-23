from rest_framework import generics, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Message,Chat
from .serializers import UserSerializer, MessageSerializer,ChatSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class UserLoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # Implement user login logic using Django's authentication system
        # Return an authentication token or success message
        pass

class OnlineUsersAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # Retrieve a list of online users
        online_users = User.objects.filter(online=True).exclude(username=request.user.username)
        serializer = UserSerializer(online_users, many=True)
        return Response(serializer.data)

class ChatStartView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

class SendMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        # Add logic to set sender and receiver based on the request
        serializer.save(sender=self.request.user)

class ChatHistoryView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # Add logic to retrieve chat history for the user
        pass
