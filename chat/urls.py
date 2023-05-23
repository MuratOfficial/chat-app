from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

# app_name = 'chat'

urlpatterns = [
    path('', chat_views.chatPage, name='chat-page'),

    #login
    path('auth/login/', LoginView.as_view(template_name='chat/Login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]