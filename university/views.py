from university.models import University
from django.views.generic import CreateView
from .forms import UniversityForm


class UnivCreate(CreateView):
    model = University
    form_class = UniversityForm
    success_url= '/' # 성공시 연결할 페이지, 
    # fields = ['uni_name', 'uni_degree', 'uni_major', 'is_attending', ]
    template_name = "university/new.html"

# def home(request):
#     form = UniversityForm()
#     return = render(request, 'new.html', {'form':form})

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