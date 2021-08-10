from django.shortcuts import render
from category.models import Category
from question.models import Tag

# Create your views here.


def landing(request):
    categories = Category.objects.all()
    tags = Tag.objects.all().order_by('-hit')[:10]
    return render(
        request,
        'home/index.html',
        {
            'categories': categories,
            'tags': tags,
            'cnt': 0
        }
    )