from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'answer_desc': forms.Textarea (
                attrs={
                    'class': 'answer_desc nav-search-input',
                    'style': '''width: 500px; height: 100px; border:none; border-right:0px; border-top:0px; boder-left:0px;
                                boder-bottom:0px; margin-left: 3px;'''
                }
            )
        }