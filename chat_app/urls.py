from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('api/online-users/', views.OnlineUsersAPIView.as_view(), name='online-users'),
    # Define other chat-related API endpoints her

    path('api/chat/start/', views.ChatStartView.as_view(), name='chat-start'),
    path('api/chat/send/', views.SendMessageView.as_view(), name='send-message'),
    path('api/chat/history/', views.ChatHistoryView.as_view(), name='chat-history'),
]
