from django.shortcuts import render
from teams.models import UserTeamProfile
from home.models import Home
from story.models import Story

# user 정보 가져와서 새로 Join한 유저 위치 초기화
def get_user_init(request):
  users = UserTeamProfile.objects.select_related('user').all()
  
  for user in users:
    home_user = users.user
    if home_user.pos is None:
      home_user.pos = 0
      home_user.save()

  return render(request)
  

# 보드게임판 위 유저 위치 설정
def uesr_pos(request, user):
  if request.method == 'POST':
      # story가 활성화 되면 한칸 이동
      active_story = Story.objects.filter(user=user, is_active=True).first()
    
      if active_story:
        user.pos += 1
        user.save()

  return render(request)


# 초대 연결 버튼
