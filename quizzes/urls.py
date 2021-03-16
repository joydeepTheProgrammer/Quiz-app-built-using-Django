
from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('createQuiz/', views.createQuiz, name='createQuiz')
]
