from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
from django.urls.base import reverse_lazy
from university.models import University
from django.views.generic import CreateView
from .forms import UniversityForm


class UnivCreate(CreateView):
    model = University
    form_class = UniversityForm
    success_url= reverse_lazy('spec') # 성공시 연결할 페이지, 
    # fields = ['uni_name', 'uni_degree', 'uni_major', 'is_attending', ]
    template_name = "university/new.html"

    def form_valid(self, form): # 유저 객체 포함해서 저장
        obj = form.save(commit=False)
        if self.request.user.is_authenticated and self.request.method == 'POST':
            try:
                obj.user_id = self.request.user
                obj.save()
                return super().form_valid(form)
            except ValueError:
                return HttpResponseBadRequest()
        else:
            return HttpResponseForbidden()


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