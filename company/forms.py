from django import forms
from django.forms.widgets import CheckboxInput, TextInput
from .models import Company
from .widgets import DateInput

classValue = "form-control px-3"
styleValue = "background-color: wheat; height: 3rem;"

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['join_date', 'leave_date','comp_name', 'comp_title', 'employ_type', 'is_working']
        widgets = {
            'join_date': DateInput(attrs={
                "class": classValue, "style": styleValue
            }),
            'leave_date': DateInput(attrs={
                "class": classValue, "style": styleValue
            }),
            'comp_name': TextInput(attrs={
                "placeholder": "카카오커머스", "class": classValue, "style": styleValue
            }),
            'comp_title': TextInput(attrs={
                "placeholder": "백엔드 개발자", "class": classValue, "style": styleValue
            }),
            'employ_type': TextInput(attrs={
                "placeholder": "정규직", "class": classValue, "style": styleValue
            }),
            'is_working': CheckboxInput(attrs={
                "class": "form-check-input", "id":"isWorkingCheckBox"
            }),
        }