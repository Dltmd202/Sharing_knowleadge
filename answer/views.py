from abc import ABC

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Answer
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from category.models import Category
from question.models import Question
from .forms import AnswerForm
from question import urls
from user.models import CustomUser


class AnswerList(ListView):
    model = Answer
    template_name = 'answer/answer_list.html'
    ordering = '-pk'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnswerList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_answer_count'] = Answer.objects.filter(user_id=None).count()
        return context


class AnswerDetail(DetailView):
    model = Answer
    template_name = 'answer/answer_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnswerDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_answer_count'] = Answer.objects.filter(user_id=None).count()
        return context


def new_answer(request, pk):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=pk)

        if request.method == 'POST':
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.question_id = question
                answer.user_id = request.user
                answer.user_id.answer_count += 1
                answer.user_id.save()
                answer.save()
                return redirect(question.get_absolute_url())
        else:
            return redirect(question.get_absolute_url())
    else:
        raise PermissionDenied


def vote_answer(request, pk, answer_pk):
    current_answer = Answer.objects.get(id=answer_pk)
    question = get_object_or_404(Question, pk=pk)
    if request.user.is_authenticated:
        try:
            vote_user = current_answer.vote_user.get(username=request.user)
            current_answer.vote_user.remove(request.user)
        except:
            current_answer.vote_user.add(request.user)
        current_answer.save()
        return redirect(question.get_absolute_url())
    else:
        raise PermissionDenied


def select_answer(request, pk, answer_pk):
    current_answer = Answer.objects.get(id=answer_pk)
    answered_user = current_answer.user_id
    question = get_object_or_404(Question, pk=pk)
    if not question.who_chosen and not question.user_id == answered_user:
        question.who_chosen = current_answer.user_id
        current_answer.is_chosen = True
        answered_user.answer_point = str(int(answered_user.left_ans_point() + int(question.get_ques_point())))
        answered_user.chosen_count += 1
        current_answer.save()
        answered_user.save()
        question.save()
        return redirect(question.get_absolute_url())
    else:
        raise PermissionDenied


class AnswerEdit(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = ['answer_title', 'answer_desc']
    template_name = 'answer/answer_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(AnswerEdit, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class AnswerSearch(AnswerList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        answer_list = Answer.objects.filter(
            Q(answer_title__contains=q) | Q(answer_desc__contains=q)
        ).distinct()
        return answer_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnswerSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search : {q} ({self.get_queryset().count()}'
        return context





# def home(request):
#     answers = Answer.objects.all()
#     return render(request, 'edit.html', {'answers': answers})


# def new(request):
#     return render(request, 'new.html')


# def create(request):
#     new_answer = Answer()
#     new_answer.answer_title = request.POST['editor']
#     new_answer.answer_desc = request.POST['body']
#     new_answer.answer_date = timezone.now()
#     new_answer.save()
#     return redirect('edit', new_answer.id)


# def edit(request,id):
#     edit_answer = Answer.objects.get(id=id)
#     return render(request, 'edit.html', {'answer': edit_answer})


# def detail(request,id):
#     answer = get_object_or_404(Answer,pk=id)
#     return render(request,'detail.html',{'answer':answer})