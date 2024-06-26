from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, SignalLog
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Message)
def log_message(sender, instance, created, **kwargs):
    if created:
        log_entry = f'Message "{instance.content}" sent by {instance.author.username} in chat "{instance.chat.name}"'
        logger.info(log_entry)
        SignalLog.objects.create(message=log_entry)
