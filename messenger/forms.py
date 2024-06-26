from django import forms
from django.contrib.auth.models import User
from .models import Chat, Message

class ChatForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Chat
        fields = ['name', 'users']

class MessageForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ['content', 'author']
