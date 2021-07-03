from django import forms
from .models import University
from .widgets import DateInput

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['enter_date', 'grad_date','uni_name', 'uni_degree', 'uni_major', 'is_attending']
        widgets = {
            'enter_date': DateInput(),
            'grad_date': DateInput(),
        }