from django.contrib import admin
from .models import Chat, Message, SignalLog

class ChatAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['users']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'chat', 'content', 'timestamp']

class SignalLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'message']

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(SignalLog, SignalLogAdmin)
