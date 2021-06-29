from django.db import models

# Create your models here.


class Category(models.Model):
    user_id = models.IntegerField(null=True, blank=True, on_delete=models.SET_NULL)
    post_date = models.DateField(null=False, blank=False)
    modify_date = models.DateField(null=False, blank=False)
    ques_desc = models.CharField(null=True, max_length=50)
    