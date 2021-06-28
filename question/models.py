from django.db import models
from user.models import CustomUser
from category.models import Category


#User 모델 완성 후 수정할 것
class Question(models.Model):
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    ques_desc = models.TextField()
    ques_title = models.CharField(max_length=30)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return f'/question/{self.pk}/'
