from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['ques_title', 'category_id', 'ques_point', 'ques_desc', 'head_img', 'tags']
        widgets = {
            'ques_title': forms.TextInput(
                attrs={
                    'class': 'custom-contentview question_form',
                }
            ),
            'category_id': forms.Select(
                attrs={
                    'class': 'custom-contentview question_form',
                }
            ),
            'ques_point': forms.TextInput(
                attrs={
                    'class': 'custom-contentview question_form',
                }
            ),
            'ques_desc': forms.Textarea(
                attrs={
                    'class': 'custom-contentview question_form',
                    'style': '''
                                width: 1000px; 
                            '''
                }
            )
        }
