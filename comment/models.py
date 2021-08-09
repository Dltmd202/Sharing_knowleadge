from django.db import models
from answer.models import Answer
from user.models import CustomUser

class Comment(models.Model):
    answer_id = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)
    comment_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    comment_desc = models.TextField()

    def __str__(self):
        return str(self.comment_desc)

    def get_absolute_url(self):
        return f'/comment/{self.pk}/'