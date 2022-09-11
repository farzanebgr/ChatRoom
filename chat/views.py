from django.shortcuts import render
from chat.models import Room


# Display the list page and get all the rooms to show users
def index_view(request):
    context = {
        'rooms': Room.objects.all(),
    }
    return render(request, 'chat/index.html', context)

# Show a specific room or create a new room to show users
def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context = {
        'room': chat_room,
    }
    return render(request, 'chat/room.html', context)

