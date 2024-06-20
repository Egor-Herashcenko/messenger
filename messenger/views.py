from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import ChatForm, MessageForm

@login_required
def chat_list(request):
    chats = Chat.objects.all()
    return render(request, 'messenger/chat_list.html', {'chats': chats})

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all()
    return render(request, 'messenger/chat_detail.html', {'chat': chat, 'messages': messages})

@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = ChatForm()
    return render(request, 'messenger/chat_form.html', {'form': form})

@login_required
def edit_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        form = ChatForm(request.POST, instance=chat)
        if form.is_valid():
            form.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = ChatForm(instance=chat)
    return render(request, 'messenger/chat_form.html', {'form': form})

@login_required
def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        chat.delete()
        return redirect('chat_list')
    return render(request, 'messenger/chat_confirm_delete.html', {'chat': chat})

@login_required
def create_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.author = request.user
            message.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = MessageForm()
    return render(request, 'messenger/message_form.html', {'form': form, 'chat': chat})
