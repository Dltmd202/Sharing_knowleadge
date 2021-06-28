from django.db import models
from django.contrib.auth.modles import User
from question.modles import Question
from user.models import CustomUser

class Answer(models.Model):
    question_id = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    answer_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    vote_count= models.IntegerField(default=True)
    is_chosen=models.BooleanField(default=False)
    answer_title = models.CharField(null=True, max_length=100)
    answer_desc = models.TextField(null=True)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return f'/answer/{self.pk}/'