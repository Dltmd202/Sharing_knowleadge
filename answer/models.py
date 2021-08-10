from django.db import models
from django.contrib.auth.models import User
from question.models import Question
from user.models import CustomUser


class Answer(models.Model):
    question_id = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    answer_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    is_vote = models.BooleanField(default=False)
    is_chosen = models.BooleanField(default=False)
    answer_title = models.CharField(null=True, max_length=100)
    answer_desc = models.TextField(null=True)
    vote_user = models.ManyToManyField(CustomUser, null=True,
                                       blank=True, related_name="vote_user", default=None)

    def __str__(self):
        return str(self.pk) + ': ' + self.answer_title

    def get_absolute_url(self):
        return f'/answer/{self.pk}/'

    def get_vote_count(self):
        return (self.vote_user)