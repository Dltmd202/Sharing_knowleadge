from django.shortcuts import render
from category.models import Category

# Create your views here.


def landing(request):
    categories = Category.objects.all()
    return render(
        request,
        'home/index.html',
        {
            'categories': categories,
            'cnt': 0
        }
    )