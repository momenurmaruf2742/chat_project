from django.urls import path
from . import api_views,views

urlpatterns = [
    path('', views.RegistrationView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),



    path('api/register/', api_views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/login/', api_views.UserLoginAPIView.as_view(), name='user-login'),
    path('api/online-users/', api_views.OnlineUsersAPIView.as_view(), name='online-users'),
    # Define other chat-related API endpoints her

    path('api/chat/start/', api_views.ChatStartView.as_view(), name='chat-start'),
    path('api/chat/send/', api_views.SendMessageView.as_view(), name='send-message'),
    path('api/chat/history/', api_views.ChatHistoryView.as_view(), name='chat-history'),
]
