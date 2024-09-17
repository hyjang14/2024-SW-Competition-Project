# story/views.py
from django.shortcuts import render
from .models import User
from .models import Story
from .models import Home
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')  # 로그인 페이지로 리다이렉트
def board_view(request):
    return render(request, 'board.html')

def story_view(request):
    # POST 요청에서 'room_id' 값을 가져옴
    room_id = request.POST.get('room_id')
    user = request.user
    character = user.character
    stories = Story.objects.filter(room_id=request.POST.get('room_id'))

    return render(request, 'story.html', {
        'character': character,
        'stories': stories,
        })

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']

        return HttpResponse('성공')
    return HttpResponse('실패')