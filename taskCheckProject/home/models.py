from django.db import models
from django.utils import timezone
from teams.models import UserTeamProfile


# Create your models here.
class Home(models.Model):
  rood_id = models.IntegerField(primary_key=True)
  goal = models.CharField(max_length=500)
  date = models.DateField(default=timezone.now)
  start_date = models.DateField(default=timezone.now)
  end_date = models.DateField(default=timezone.now)
  image = models.CharField(max_length=150)
  pos = models.IntegerField(null=True, blank=True)
  is_end = models.BooleanField()
  invitation_num = models.IntegerField()
  user_id = models.ForeignKey(UserTeamProfile, on_delete=models.CASCADE)

  def __str__(self):
    return self.goal