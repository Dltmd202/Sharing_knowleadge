from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_desc']
        widgets = {
            'comment_desc': forms.Textarea(
                attrs={
                    'class': 'comment_desc nav-search-input',
                    'style': '''width: 400px; height: 40px; border:none; border-right:0px; border-top:0px; boder-left:0px;
                                boder-bottom:0px; margin-left: 3px;'''
                }
            )
        }
