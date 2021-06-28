from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Question(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    ques_desc = models.TextField()
    ques_title = models.CharField(max_length=30)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return f'/question/{self.pk}/'
