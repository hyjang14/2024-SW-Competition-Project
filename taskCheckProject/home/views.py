# home > views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from teams.models import UserTeamProfile, Team
from .models import Home
from story.models import Story

def update_home(request, team_id):
  team=get_object_or_404(Team, id=team_id)
  home = get_object_or_404(Home, team=team)

  if request.method == 'POST':
      # n일차 계산
    today = timezone.now().date()
    delta = (today - home.start_date.date()).days   #오늘날짜-시작일 차이
    home.date = delta + 1  # 1일차부터 시작해서 +1
    home.save()
  
    return redirect('teams:team_detail', team_id=team_id)
      
  return render(request, 'team_detail.html', {
     'team': team,
     'home': home
     })




# 보드게임판 칸 리스트 생성
def board_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    duration = team.duration

    # 행 개수 계산 (5일당 2줄)
    rows = (duration // 5) * 2 + (1 if duration % 5 > 0 else 0)

    print(f"Calculated rows: {rows}")  # 디버깅용으로 출력

    # range(4)를 템플릿으로 전달
    columns = range(4)

    return render(request, 'teams/team_detail.html', {
        'rows': range(rows),
        'columns': columns,  # range(4)를 템플릿에 넘김
        'duration': duration,
        'team': team,
    })

  

# 보드게임판 위 유저 위치 설정
def user_pos(request, home_id):
  home = get_object_or_404(Home, id=home_id)

  if request.method == 'POST':
      users = UserTeamProfile.objects.all()

      for user in users:
        # story가 활성화 되면 한칸 이동
        active_story = Story.objects.filter(user=user, is_active=True).first()
    
        if active_story:
          current_pos = home.positions.get(str(user.id), 0)
          home.positions[str(user.id)] = current_pos + 1
      
      home.save()

  users = UserTeamProfile.objects.select_related('User').all()
  return render(request, 'teams/team-detail.html', {'users': users})