from django import forms
from .models import University


class DateInput(forms.DateInput):
    input_type = 'date'

    class UniversityForm(forms.ModelForm):
        class Meta:
            model = University
            fields = ['enter_date', 'grad_date',]
            widgets = {
                'enter_date': forms.DateInput(),
                'grad_date': forms.DateInput(),
            }