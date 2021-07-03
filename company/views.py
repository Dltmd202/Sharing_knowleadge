from company.models import Company
from django.views.generic import CreateView
from .forms import CompanyForm

class CompCreate(CreateView):
    model = Company
    form_class = CompanyForm
    success_url= '/' # 성공시 연결할 페이지, 
    template_name = "company/new.html"