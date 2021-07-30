from abc import ABC

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Answer, Comment
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from category.models import Category
from question.models import Question
from .forms import AnswerForm, CommentForm
from question import urls
from user.models import CustomUser


# 코멘트 만들기
class CommentCreate(LoginRequiredMixin, CreateView, ABC):
    def new_comment(request, pk):
        filled_form = CommentForm(request.Post)
        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            finished_form.post = get_object_or_404(Answer, pk=pk)
            finished_form.save()
        return redirect('detail', pk)

    def detail(request, pk):
        post_detail = get_object_or_404(Answer, pk=pk)
        comment_form = CommentForm()
        return render(request,'question_detail.html',{'post_detail': post_detail, 'comment_form': comment_form})


class CommentEdit(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['comment_data', 'comment_desc']
    template_name = 'answer/answer_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(CommentEdit, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
