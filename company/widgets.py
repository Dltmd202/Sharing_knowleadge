from django import forms
from .models import Company


class DateInput(forms.DateInput):
    input_type = 'date'

    class UniversityForm(forms.ModelForm):
        class Meta:
            model = Company
            fields = ['join_date', 'leave_date',]
            widgets = {
                'join_date': forms.DateInput(),
                'leave_date': forms.DateInput(),
            }