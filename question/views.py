from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Question
from category.models import Category


class QuestionList(ListView):
    model = Question
    template_name = 'question/question_list.html'
    ordering = '-pk'
    paginate_by = 5


class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/question_detail.html'



class QuestionCreate():
    pass


class QuestionUpdate():
    pass

