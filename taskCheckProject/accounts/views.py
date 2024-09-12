from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


# 임시 홈화면(로그인 후 렌더되는 화면)
def home(request):
    return render(request, 'home.html')

# 회원가입
def join(request):
    if request.method=='POST':
        if request.POST['password'] == request.POST['repeat']:
            first_name = request.POST['first_name']
            new_user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                first_name=first_name,)
            print('회원가입 성공')

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
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."  # 에러 메시지 설정
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')