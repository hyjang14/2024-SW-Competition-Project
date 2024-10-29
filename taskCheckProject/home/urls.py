#home/urls.py
from django.urls import path
from home import views 
app_name = 'home'

urlpatterns = [
    path('completion/<int:team_id>/', views.completion, name='completion'),
]