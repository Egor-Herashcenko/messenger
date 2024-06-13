from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Chat(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author}: {self.content[:20]}"

    class Meta:
        permissions = [
            ("can_edit_message", "Can edit message"),
            ("can_delete_message", "Can delete message"),
        ]
