from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import RoomPost, Message
from .forms import RoomPostForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def loginPage(request):
    page  = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Username or password does not exist')

    context = {
        'page': page
    }
    return render(request, 'kyaloedua/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration.')

    return render(request, 'kyaloedua/login_register.html', {'form': form})

def about(request):
    return render(request, 'kyaloedua/about.html')

def room(request, pk):
    room = get_object_or_404(RoomPost, id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants,
    }
    room.participants.add(request.user)
    return render(request, 'kyaloedua/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomPostForm()
    if request.method == 'POST':
        form = RoomPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
            'form': form,
        }
    return render(request, 'kyaloedua/room_form.html', context)

@login_required(login_url='login')
def update_room(request, pk):
    room = get_object_or_404(RoomPost, id=pk)
    form = RoomPostForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        form = RoomPostForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'kyaloedua/room_form.html', context)

@login_required(login_url='login')
def delete_room(request, pk):
    room = get_object_or_404(RoomPost, id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'kyaloedua/delete.html', {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = get_object_or_404(Message, id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'kyaloedua/delete.html', {'obj': message})








