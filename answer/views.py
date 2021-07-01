from abc import ABC

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Answer
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from category.models import Category
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


class AnswerNew(LoginRequiredMixin, CreateView, ABC):
    model = Answer
    fields = ['answer_title', 'answer_desc', 'question_id', 'vote_count']
    template_name = 'answer/answer_new.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            vote_count_str = self.request.POST.get('vote_count')
            vote_count_str = form.fields['vote_count']
            new_answer = CustomUser()
            if vote_count_str:
                user = CustomUser.objects.get(username=current_user)

                user.answer_point = str(int(user.left_answer()) - int(self.request.POST.get('vote_count')))
                user.save()
            return super(AnswerNew, self).form_valid(form)
        else:
            return redirect('/answer')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnswerNew, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_answer_count'] = Answer.objects.filter(category_id=None).count()
        return context

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