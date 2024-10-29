from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from teams.models import Team
from home.models import Home
from django.core.paginator import Paginator
from django.contrib import messages


# 홈화면(로그인 후 렌더되는 화면)
def home(request):
    # 진행 중인 방과 마감된 방 필터링
    ongoing_homes = Home.objects.filter(is_end=False)  
    ended_homes = Home.objects.filter(is_end=True) 

    # 페이지네이션
    ongoing_paginator = Paginator(ongoing_homes, 3)  
    ended_paginator = Paginator(ended_homes, 3) 

    ongoing_page_number = request.GET.get('ongoing_page') 
    ended_page_number = request.GET.get('ended_page')   

    ongoing_page_obj = ongoing_paginator.get_page(ongoing_page_number) 
    ended_page_obj = ended_paginator.get_page(ended_page_number)  

    return render(request, 'home.html', {
        'ongoing_page_obj': ongoing_page_obj,
        'ended_page_obj': ended_page_obj,
    })


# 회원가입
def join(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat']
        first_name = request.POST['first_name']

        # 사용자 이름 중복 확인
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 가입된 사용자입니다.')
            return render(request, 'join.html')

        # 비밀번호 확인
        if password != repeat_password:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'join.html')

        # 새로운 사용자 생성
        new_user = User.objects.create_user(
            username=username, 
            password=password,
            first_name=first_name,
        )
        print('회원가입 성공')
        messages.success(request, '회원가입이 성공적으로 완료되었습니다.')
        return redirect('accounts:start')
    
    return render(request, 'join.html')



# 회원가입 성공
def start(request):
    return render(request, 'start.html')

# 로그인
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('accounts:home')
        else: 
            error_message = "아이디 또는 비밀번호가 잘못되었습니다." 
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
    
# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
