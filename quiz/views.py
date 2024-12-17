from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import QuizSession
from question.models import Question
import random

# Create your views here.
def start_quiz(request):
    # Start a new quiz session.
    session = QuizSession.objects.create()
    return JsonResponse({
        'message': 'New quiz session started.',
        'session_id': session.id
    })

def get_random_question(request, session_id):
    # Retrieve a random question.
    session = get_object_or_404(QuizSession, id=session_id)
    questions = Question.objects.all()

    if not questions.exists():
        return JsonResponse({'error': 'No questions available in the database.'}, status=404)

    question = random.choice(questions)
    return JsonResponse({
        'question_id': question.id,
        'text': question.text,
        'options': {
            'A': question.option_a,
            'B': question.option_b,
            'C': question.option_c,
            'D': question.option_d
        }
    })

def submit_answer(request, session_id, question_id):
    # Submit an answer for a question.
    session = get_object_or_404(QuizSession, id=session_id)
    question = get_object_or_404(Question, id=question_id)

    user_answer = request.GET.get('answer')
    if not user_answer or user_answer not in ['A', 'B', 'C', 'D']:
        return JsonResponse({'error': 'Invalid answer. Must be one of A, B, C, D.'}, status=400)

    session.total_questions += 1

    if user_answer == question.correct_option:
        session.correct_answers += 1
        result = 'correct'
    else:
        session.incorrect_answers += 1
        result = 'incorrect'

    session.save()

    return JsonResponse({
        'message': f'Your answer is {result}.',
        'correct_option': question.correct_option
    })

def quiz_summary(request, session_id):
    # Get the summary of the quiz session.
    session = get_object_or_404(QuizSession, id=session_id)

    return JsonResponse({
        'total_questions_answered': session.total_questions,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers
    })