from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
from django.urls.base import reverse_lazy
from company.models import Company
from django.views.generic import CreateView
from .forms import CompanyForm

class CompCreate(CreateView):
    model = Company
    form_class = CompanyForm
    success_url= reverse_lazy('spec') # 성공시 연결할 페이지, 
    template_name = "company/new.html"

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