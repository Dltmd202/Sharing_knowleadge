from abc import ABC

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from category.models import Category


# 작동 문제 없음
class QuestionList(ListView):
    model = Question
    template_name = 'question/question_list.html'
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_question_count'] = Question.objects.filter(category_id=None).count()
        return context


# 작동 문제 없음
class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/question_detail.html'


# 작동 문제 없음
class QuestionCreate(LoginRequiredMixin, CreateView, ABC):
    model = Question
    fields = ['ques_title', 'category_id', 'ques_desc', 'head_img']
    template_name = 'question/question_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(QuestionCreate, self).form_valid(form)
        else:
            return redirect('/question')


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['ques_title', 'category_id', 'ques_desc', 'head_img']
    template_name = 'question/question_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(QuestionUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class QuestionSearch(QuestionList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        question_list = Question.objects.filter(
            Q(ques_title__contains=q) | Q(ques_desc__contains=q)
        ).distinct()
        return question_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search : {q} ({self.get_queryset().count()}'
        return context