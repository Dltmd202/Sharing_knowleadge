from django.db import models
from answer.models import Answer

class Comment(models.Model):
    answer_id = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True)
    comment_desc = models.TextField(null=True)

    def __str__(self):
        return str(self.pk) + ': ' + self.answer_id

    def get_absolute_url(self):
        return f'/question/{self.pk}/'
