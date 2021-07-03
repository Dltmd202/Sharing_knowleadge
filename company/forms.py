from django import forms
from .models import Company
from .widgets import DateInput

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['join_date', 'leave_date','comp_name', 'comp_title', 'employ_type', 'is_working']
        widgets = {
            'join_date': DateInput(),
            'leave_date': DateInput(),
        }