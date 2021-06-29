from django.db import models
from user.models import CustomUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=1200, unique=True, allow_unicode=True)