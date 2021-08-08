from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['ques_title', 'category_id', 'ques_point', 'ques_desc', 'head_img']
        widgets = {
            'ques_title': forms.TextInput(
                attrs={
                    'class': 'question__input question_form',
                }
            ),
            'category_id': forms.Select(
                attrs={
                    'class': 'question__input question_form',
                }
            ),
            'ques_point': forms.TextInput(
                attrs={
                    'type': "number",
                    'id': 'question__input__point',
                    'class': 'question__input question_form',
                }
            ),
            'ques_desc': forms.Textarea(
                attrs={
                    'id': 'question__input__content',
                    'class': 'question__input question_form',
                }
            )
        }
