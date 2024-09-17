# story/models.py
from django.db import models
from django.contrib.auth.models import User
from home.models import Home
from django.contrib.auth.models import AbstractUser

class Story(models.Model):
    # story_id = models.PublicKey 
    # story_id는 장고에서 자동으로 기본 키 생성해줌
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # 부모 객체가 삭제될 때 자식도 같이 삭제됨
    username = models.CharField(max_length=500) # varchar(500)
    post = models.ImageField(upload_to='story_images/')
    expire_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    room_id = models.ForeignKey(Home, on_delete=models.CASCADE)

    def __str__(self):
        return f"Story by {self.user.username}"