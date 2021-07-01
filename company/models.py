from django.db import models
from user.models import CustomUser

class Company(models.Model):
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    comp_name = models.CharField(max_length=50) 
    comp_title = models.CharField(max_length=50)
    employ_type = models.CharField(max_length=50)
    join_date = models.DateField()
    leave_date = models.DateField(null=True, blank = True) 
    is_working = models.BooleanField()