from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_desc = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    ques_point = models.IntegerField(default=0, null=False, blank=False)
    answer_point = models.IntegerField(default=0, null=False, blank=False)
    account = models.IntegerField(default=0, null=False, blank=False)
    score = models.IntegerField(default=0, null=False, blank=False)
    user_pic = models.ImageField(upload_to='user_pics', null=True, blank=True) # pip install pillow 해야함
    user_pic_url = models.URLField(default=None, null=True, blank=True) # 사진을 url로 저장하기 위함

    REQUIRED_FIELDS = []

    # question의 ques_point 문자열 호출용
    def left_ques(self):
        return self.ques_point