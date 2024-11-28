from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Default route
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz, name='quiz'),
]
