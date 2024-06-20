from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('create/', views.create_chat, name='create_chat'),
    path('<int:chat_id>/edit/', views.edit_chat, name='edit_chat'),
    path('<int:chat_id>/delete/', views.delete_chat, name='delete_chat'),
    path('<int:chat_id>/message/', views.create_message, name='create_message'),
]
