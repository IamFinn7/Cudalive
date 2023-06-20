from django.http import HttpResponse
from django.shortcuts import render
from .models import Room, Message

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, id):
    all_rooms = Room.objects.exclude(id=id)
    room = Room.objects.get(id=id)

    playlist = room.playlist_set.all()

    messages = Message.objects.filter(room = room)

    context = {'videos': playlist, 'all_rooms': all_rooms, 'room': room, 'messages': messages}
    
    return render(request, 'base/room_form.html', context)

def login(request):
    return render(request, 'base/login.html')