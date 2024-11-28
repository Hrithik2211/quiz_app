# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .models import Question
# import random


from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')


def quiz(request):
    return render(request, 'quiz.html')

# def dashboard(request):
#     user_stats = request.session.get('stats', {'attempted': 0, 'correct': 0})
#     percentage = (user_stats['correct'] / user_stats['attempted']
#                   * 100) if user_stats['attempted'] > 0 else 0
#     return render(request, 'dashboard.html', {
#         'stats': user_stats,
#         'percentage': percentage,
#     })


# def quiz(request):
#     if request.method == 'GET':
#         question = random.choice(Question.objects.all())
#         return render(request, 'quiz.html', {'question': question})

#     if request.method == 'POST':
#         question_id = int(request.POST['question_id'])
#         selected_option = request.POST['selected_option']
#         question = Question.objects.get(id=question_id)

#         is_correct = (selected_option == question.correct_option)
#         stats = request.session.get('stats', {'attempted': 0, 'correct': 0})
#         stats['attempted'] += 1
#         if is_correct:
#             stats['correct'] += 1
#         request.session['stats'] = stats

#         return JsonResponse({'is_correct': is_correct})
