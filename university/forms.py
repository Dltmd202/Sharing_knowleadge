from django import forms
from .models import University
from .widgets import DateInput
from django.forms.widgets import CheckboxInput, TextInput

classValue = "form-control px-3"
styleValue = "background-color: wheat; height: 3rem;"

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['enter_date', 'grad_date','uni_name', 'uni_degree', 'uni_major', 'is_attending']
        widgets = {
            'enter_date': DateInput(attrs={
                "class": classValue, "style": styleValue
            }),
            'grad_date': DateInput(attrs={
                "class": classValue, "style": styleValue
            }),
            'uni_name': TextInput(attrs={
                "placeholder": "서울대학교", "class": classValue, "style": styleValue
            }),
            'uni_degree': TextInput(attrs={
                "placeholder": "석사", "class": classValue, "style": styleValue
            }),
            'uni_major': TextInput(attrs={
                "placeholder": "컴퓨터공학과", "class": classValue, "style": styleValue
            }),
            'is_attending': CheckboxInput(attrs={
                "class": "form-check-input", "id":"isAttendingCheckBox"
            }),
        }