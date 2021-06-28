from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Question
from category.models import Category


class QuestionList(ListView):
    model = Question
    ordering = '-pk'
    paginate_by = 5


class QuestionDetail(DetailView):
    model = Question


class QuestionCreate():
    pass


class QuestionUpdate():
    pass

