from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_title', 'answer_desc']
        widgets = {
            'answer_title': forms.TextInput(
                attrs={
                    'class': 'question__input question_form',
                }
            ),
            'answer_desc': forms.Textarea(
                attrs={
                    'class': 'question__input question_form',
                    'id': 'answer__input'
                }
            )
        }
