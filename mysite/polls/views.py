from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader  # noqa: F401, needed for render shortcut

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)  # usage of shortcut
    return render(request, 'polls/detail.html', {'question': q})


def results(request, question_id):
    resp = f"You're looking at the results of question {question_id}."
    return HttpResponse(resp)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")