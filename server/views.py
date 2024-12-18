from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Question
import random


def start_quiz(request):
    # Initialize session variables for score and total questions
    request.session['score'] = 0
    request.session['total_questions'] = 0
    return render(request, 'start.html')


def get_question(request):
    # Get a random question
    question = random.choice(Question.objects.all())
    return render(request, 'question.html', {'question': question})


def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        selected_answer = request.POST['answer']

        question = get_object_or_404(Question, pk=question_id)

        # Update score and total questions in session
        request.session['total_questions'] += 1
        if selected_answer == question.correct_answer:
            request.session['score'] += 1

        return render(request, 'result.html', {'question': question, 'selected_answer': selected_answer, 'score': request.session['score'],
                                               'total_questions': request.session['total_questions']})


def get_score(request):
    # Retrieve score from the session
    score = request.session.get('score', 0)
    total_questions = request.session.get('total_questions', 0)
    return JsonResponse({'score': score, 'total_questions': total_questions})


def get_score(request):
    # Retrieve score and total questions answered from the session
    score = request.session.get('score', 0)
    total_questions = request.session.get('total_questions', 0)

    # Render the score page
    return render(request, 'score.html', {'score': score, 'total_questions': total_questions})
