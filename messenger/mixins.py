from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, Message
from datetime import timedelta
from django.utils import timezone

class UserIsMemberMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        if request.user not in chat.members.all():
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class UserIsAuthorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        message = get_object_or_404(Message, id=self.kwargs['pk'])
        if message.author != request.user:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class SuperUserRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class ChatOwnerMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        if chat.owner != request.user:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class MessageOwnerOrSuperUserMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        message = get_object_or_404(Message, id=self.kwargs['pk'])
        if message.author != request.user and not request.user.is_superuser:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class RecentMessageMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        message = get_object_or_404(Message, id=self.kwargs['pk'])
        if timezone.now() - message.timestamp > timedelta(days=1):
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class UserIsActiveMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class UserInChatMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        if request.user not in chat.members.all():
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)

class MessageEditableMixin(UserIsAuthorMixin, RecentMessageMixin):
    pass

class UserIsSuperUserMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('chat_list')
        return super().dispatch(request, *args, **kwargs)
