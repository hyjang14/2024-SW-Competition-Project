#story/urls.py
from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    path('board/', views.board_view, name='board'),  # /board 경로
    path('upload/', views.upload_image, name='upload_image'),  # 업로드 URL 정의
    path('', views.story_view, name='story_view'),  # 'story/'에 대한 패턴
]
