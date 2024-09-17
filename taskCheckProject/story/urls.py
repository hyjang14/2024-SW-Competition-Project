#story/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.board_view, name='board'),  # /board 경로
    path('upload/', views.upload_image, name='upload_image'),  # 업로드 URL 정의
]
