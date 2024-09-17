# story/views.py
from django.shortcuts import render
from .models import User
from .models import Story
# from .models import Room
def board_view(request):
    return render(request, 'board.html')

def story_view(request):
    user = request.user
    character = user.character
    stories = Story.objects.filter(room_id = room_id)

    return render(request, 'story.html', {
        'character': character,
        'stories': stories,
        })