from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import QuizSession
from question.models import Question
import random
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def start_quiz(request):
    # Start a new quiz session.
    session = QuizSession.objects.create()
    return render(request, 'quiz/start_quiz.html', {'session_id': session.id})


def get_random_question(request, session_id):
    # Retrieve a random question.
    session = get_object_or_404(QuizSession, id=session_id)
    questions = Question.objects.all()

    if not questions.exists():
        return render(request, 'quiz/error.html', {'message': 'No questions available in the database.'})

    question = random.choice(questions)
    return render(request, 'quiz/question.html', {
        'session_id': session.id,
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
    # Ensure the request is a POST request
    if request.method == 'POST':
        session = get_object_or_404(QuizSession, id=session_id)
        question = get_object_or_404(Question, id=question_id)

        # Get the user's answer from the form submission
        user_answer = request.POST.get('answer')

        # Validate the answer
        if not user_answer or user_answer not in ['A', 'B', 'C', 'D']:
            return render(request, 'quiz/error.html', {'message': 'Invalid answer. Must be one of A, B, C, D.'})

        # Update session statistics based on the user's answer
        session.total_questions += 1

        if user_answer == question.correct_option:
            session.correct_answers += 1
            result = 'correct'
        else:
            session.incorrect_answers += 1
            result = 'incorrect'

        # Save the session after updating
        session.save()

        # Return the result of the answer submission
        return render(request, 'quiz/answer_result.html', {
            'result': result,
            'correct_option': question.correct_option,
            'session_id': session.id
        })

    else:
        # If the method is not POST, return a forbidden response
        return HttpResponseForbidden("Invalid request method")

def quiz_summary(request, session_id):
    # Get the summary of the quiz session.
    session = get_object_or_404(QuizSession, id=session_id)

    return render(request, 'quiz/summary.html', {
        'total_questions_answered': session.total_questions,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers
    })