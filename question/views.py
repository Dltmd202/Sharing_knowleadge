from abc import ABC

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question
from category.models import Category


#작동 문제 없음
class QuestionList(ListView):
    model = Question
    template_name = 'question/question_list.html'
    ordering = '-pk'
    paginate_by = 5


#작동 문제 없음
class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/question_detail.html'


#Category 모델 완성 이후 테스트
class QuestionCreate(LoginRequiredMixin, CreateView, ABC):
    model = Question
    fields = ['title', 'desc', 'category']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(QuestionCreate, self).form_valid(form)
        else:
            return redirect('/question')


class QuestionUpdate():
    pass

