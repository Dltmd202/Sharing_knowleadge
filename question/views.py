from abc import ABC

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
from django.forms import formset_factory
from .models import Question
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from category.models import Category
from user.models import CustomUser
from answer.forms import AnswerForm
from django import forms
from django.db import models


# 작동 문제 없음
class QuestionList(ListView):
    model = Question
    template_name = 'question/question_list.html'
    ordering = '-pk'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_question_count'] = Question.objects.filter(category_id=None).count()
        return context


# 작동 문제 없음
class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/question_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_question_count'] = Question.objects.filter(category_id=None).count()
        context['answer_form'] = AnswerForm
        return context


# 작동 문제 없음
class QuestionCreate(LoginRequiredMixin, CreateView, ABC):
    model = Question
    fields = ['ques_title', 'category_id', 'ques_point', 'ques_desc', 'head_img']
    template_name = 'question/question_form.html'
    widgets = {
        'ques_title': forms.TextInput(
            attrs={
                'style': 'width: 600px;',
                'placeholder': 'Name'
            }
        )
    }

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.user_id = current_user
            ques_point_str = self.request.POST.get('ques_point')
            ques_point_str = form.fields['ques_point']
            new_ques = CustomUser()
            if ques_point_str:
                user = CustomUser.objects.get(username=current_user)

                user.ques_point = str(int(user.left_ques()) - int(self.request.POST.get('ques_point')))
                user.save()
            return super(QuestionCreate, self).form_valid(form)
        else:
            return redirect('/question')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionCreate, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_question_count'] = Question.objects.filter(category_id=None).count()
        return context


# 작동 문제 없음
class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['ques_title', 'category_id', 'ques_desc', 'head_img']
    template_name = 'question/question_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(QuestionUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 작동 문제 없음
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
