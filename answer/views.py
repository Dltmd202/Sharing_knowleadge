from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Answer, answer


def home(request):
    answers = Answer.objects.all()
    return render(request, 'edit.html', {'answers':answers})

def new(request):
    return render(request,'new.html')

def create(request):
    new_answer= Answer()
    new_answer.answer_title = request.POST['editor']
    new_answer.answer_desc = request.POST['body']
    new_answer.answer_date = timezone.now()
    new_answer.save()
    return redirect('edit', new_answer.id)

def edit(request,id):
    edit_answer = Answer.objects.get(id= id)
    return render(request, 'edit.html', {'answer':edit_answer})



# def detail(request,id):
#     answer = get_object_or_404(Answer,pk=id)
#     return render(request,'detail.html',{'answer':answer})