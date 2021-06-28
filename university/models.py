from django.db import models
from user.models import CustomUser

class university(models.Model):
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    uni_name = models.CharField(max_length=50)
    uni_degree = models.CharField(max_length=50)
    uni_major = models.CharField(max_length=50)
    enter_date = models.DateTimeField(auto_now=True)
    grad_date = models.DateTimeField()
    is_attending = models.BooleanField(default=false)