from django.shortcuts import render
from question.models import Question
from .models import Category
# Create your views here.


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        question_list = Question.objects.filter(category_id=None)
    else:
        category = Category.objects.get(slug=slug)
        question_list = Question.objects.filter(category_id=category)

    return render(
        request,
        'question/question_list.html',
        {
            'object_list': question_list,
            'categories': Category.objects.all(),
            'no_category_question_count': Question.objects.filter(category_id=None).count(),
            'category': category,
        }

    )