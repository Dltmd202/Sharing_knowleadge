from django.shortcuts import render
from category.models import Category
from question.models import Tag, Question

# Create your views here.


def landing(request):
    context = dict()
    categories = Category.objects.all()
    if categories:
        context['categories'] = categories
    tags = Tag.objects.all().order_by('-hit')[:10]
    if tags:
        context['tags'] = tags
    if Question.objects.all():
        pop_question = Question.objects.order_by("-hit_count_generic__hits")[0]
        if pop_question:
            context['pop_question'] = pop_question
        current_question = Question.objects.order_by("-post_date")[0]
        if current_question:
            context['current_question'] = current_question
    context['cnt'] = 0
    return render(
        request,
        'home/index.html',
        context
    )