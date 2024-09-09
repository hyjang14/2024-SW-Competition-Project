from django.urls import path
from accounts import views

app_name = "accounts" 

urlpatterns = [
    # 회원가입
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('start/', views.start, name='start'),
    path('home/', views.home, name='home'),
]