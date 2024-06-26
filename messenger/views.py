from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Chat, Message
from .forms import ChatForm, MessageForm


@login_required
def chat_list(request):
    chats = Chat.objects.filter(users=request.user)
    return render(request, 'messenger/chat_list.html', {'chats': chats})


@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.user not in chat.users.all():
        return redirect('chat_list')

    messages_list = chat.messages.all()
    users = chat.users.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.author = request.user
            message.save()

            if chat.users.filter(is_superuser=True).exists():
                messages.success(request, 'Вы успешно отправили сообщение суперюзеру')
            else:
                messages.success(request, 'Сообщение успешно отправлено')

            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = MessageForm(initial={'author': request.user})

    return render(request, 'messenger/chat_detail.html', {
        'chat': chat,
        'messages': messages_list,
        'form': form,
        'users': users
    })


@login_required
def chat_create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.save()
            chat.users.add(request.user)
            chat.save()
            messages.success(request, 'Чат успешно создан')
            return redirect('chat_list')
    else:
        form = ChatForm()

    return render(request, 'messenger/chat_create.html', {'form': form})
