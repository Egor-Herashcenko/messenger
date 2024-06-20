from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.content[:20]}'


class Meta:
    permissions = [
        ("can_edit_message", "Can edit message"),
        ("can_delete_message", "Can delete message"),
    ]
