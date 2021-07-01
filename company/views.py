from django.shortcuts import render
from company.models import Company
from django.views.generic import CreateView

class CompCreate(CreateView):
    model = Company
    fields = ['comp_name','comp_title','employ_type','join_date','leave_date','is_working']
    template_name = "new.html"