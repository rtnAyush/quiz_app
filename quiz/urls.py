from django.urls import path
from .views import start_quiz, get_random_question, submit_answer, quiz_summary

urlpatterns = [
    path('start/', start_quiz, name='start_quiz'),
    path('question/<int:session_id>/', get_random_question, name='get_random_question'),
    path('answer/<int:session_id>/<int:question_id>/', submit_answer, name='submit_answer'),
    path('summary/<int:session_id>/', quiz_summary, name='quiz_summary'),
]