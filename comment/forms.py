from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_desc']
        widgets = {
            'comment_desc': forms.Textarea(
                attrs={
                    'class': 'question__input question_form',
                }
            )
        }
