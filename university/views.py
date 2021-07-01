from django.shortcuts import render, redirect
from university.models import University
from django.views.generic import CreateView


class UnivCreate(CreateView):
    model = University
    fields = ['uni_name', 'uni_degree', 'uni_major', 'enter_date', 'grad_date', 'is_attending']
    template_name = "university/new.html"
    

# def new(request):
#     return render(request, 'new.html')

# def univ_add(request):
#     new_univ = University()
#     new_univ.uni_name = request.POST['uni_name']
#     new_univ.uni_degree = request.POST['uni_degree']
#     new_univ.uni_major = request.POST['uni_major']
#     new_univ.enter_date = request.POST['enter_date']
#     new_univ.grad_date = request.POST['grad_date']
#     new_univ.is_attending = request.POST['is_attending']
#     new_univ.save()
#     return redirect('home')