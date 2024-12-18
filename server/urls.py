from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('score/', views.get_score, name='get_score'),
]
