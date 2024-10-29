# home > views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from teams.models import Team
from .models import Home

# team 정보에 맞춰 home 업데이트
def update_home(request, team_id):
    team=get_object_or_404(Team, id=team_id)
    home = get_object_or_404(Home, team=team)

    # n일차 계산
    today = timezone.now().date()
    delta = (today - home.start_date).days 
    home.date = delta + 1 
    home.save()
        
    # 방 종료
    if home.date > team.duration:
        home.is_end = True
        home.save()
        return redirect('home:completion', team_id=team_id) 

    return None 


# 보드게임판 칸 리스트 생성
def board_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    duration = team.duration

    # 행 개수 계산 (5일당 2줄)
    rows = (duration // 5) * 2 + (1 if duration % 5 > 0 else 0) 
    columns = 4
    # 게임판 모양 2차원 배열 초기화
    board = [[-1 for _ in range(columns)] for _ in range(rows)]

    # s자 모양으로 1 배치
    count = 0
    for row in range(rows):
        if count >= duration: 
            break
        
        if row % 4 == 0:  # 0, 4, 8 ... 번째 행 
            for col in range(columns):
                if count < duration:
                    board[row][col] = count
                    count += 1
        elif row % 4 == 1:  # 1, 5 ... 번째 행 
            board[row][columns - 1] = count
            count += 1
        elif row % 4 == 2:  # 2, 6 ... 번째 행 
            for col in range(columns - 1, -1, -1):
                if count < duration:
                    board[row][col] = count
                    count += 1
        elif row % 4 == 3:  # 3, 7 ... 번째 행 
            board[row][0] = count
            count += 1

    flipped_board = board[::-1]  

    return {
        'rows': range(rows),
        'team': team,
        'board': flipped_board,
    }


# 방 종료 화면
def completion(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    home = get_object_or_404(Home, team=team)

    if home.is_end: 
        return render(request, 'completion.html', {'team': team})

    return None  