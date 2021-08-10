from django.shortcuts import render
from category.models import Category
from question.models import Tag, Question

# Create your views here.


def landing(request):
    categories = Category.objects.all()
    tags = Tag.objects.all().order_by('-hit')[:10]
    pop_question = Question.objects.order_by("-hit_count_generic__hits")[0]
    return render(
        request,
        'home/index.html',
        {
            'categories': categories,
            'tags': tags,
            'pop_question': pop_question,
            'cnt': 0
        }
    )