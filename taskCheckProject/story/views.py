# story/views.py
from django.shortcuts import render, redirect
from .models import User, Story
from home.models import Home
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from teams.models import Team, UserTeamProfile

@login_required(login_url='accounts:login')  # 로그인 페이지로 리다이렉트
def board_view(request):
    return render(request, 'board.html')

def story_view(request):
    # Simulate logged-in user for testing
    if not request.user.is_authenticated:
        user = User.objects.filter(username='testuser').first()  
    else: 
        user = request.user

    # Retrieve character image and stories for the user
    try:
        user_profile = UserTeamProfile.objects.get(user=user)
        character_image = user_profile.character_image
        upload_image = user_profile.upload_img.url if user_profile.upload_img else None
    except UserTeamProfile.DoesNotExist:
        upload_image = None

    # Retrieve stories (this might depend on your specific logic)
    stories = Story.objects.filter(room_id=request.POST.get('room_id', None))

    return render(request, 'story.html', {
        'character': character_image,
        'stories': stories,
    })

def upload_image(request):
    # Simulate getting a test user using 'username' instead of 'code'
    test_user, created = User.objects.get_or_create(username='testuser', defaults={
        'email': 'testuser@example.com',
        'password': 'testpwd',
    })

    # Use test user for testing instead of request.user
    # user = request.user
    user = test_user

    # Ensure a team exists or create a default one using 'name' field
    team, created = Team.objects.get_or_create(code='defaultCode', defaults={'name': 'defaultTeam', 'duration': 30})

    if request.method == 'POST' and 'img' in request.FILES:
        image = request.FILES['img']
        print("업로드 이미지 :", image)

        # Update or create the test user's profile and assign a team
        user_profile, created = UserTeamProfile.objects.get_or_create(user=user)
        user_profile.character_image = image
        user_profile.save()

        return redirect('story:story_view')
    return render(request, 'upload_form.html')


def story_view(request):
    # 테스트 데이터
    user = request.user
    if not user.is_authenticated:
        user = User.objects.first()

    # team, created = Team.objects.get_or_create(name='testTeam', defaults={'duration': 30})
    try:
        user_profile = UserTeamProfile.objects.get(user=user)
        upload_image = user_profile.upload_img.url if user_profile.upload_img else None
        print(upload_image)  # Check the URL of the uploaded image
    except UserTeamProfile.DoesNotExist:
        upload_image = None
        #user_profile = UserTeamProfile.objects.create(user=user, team=team)
    
    return render(request, 'board.html', {'upload_img': upload_image,})