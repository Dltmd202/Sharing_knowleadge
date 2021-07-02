from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_title', 'answer_desc']
        widgets = {
            'answer_title': forms.TextInput(
                attrs={
                    'class': 'answer-title nav-search-input',
                    'style': '''width: 550px; border:none; border-right:0px; border-top:0px; boder-left:0px;
                                boder-bottom:0px; margin-left: 3px;'''
                }
            ),
            'answer_desc': forms.Textarea(
                attrs={
                    'class': 'answer_desc nav-search-input',
                    'style': '''width: 550px; height: 300px; border:none; border-right:0px; border-top:0px; boder-left:0px;
                                boder-bottom:0px; margin-left: 3px;'''
                }
            )
        }
