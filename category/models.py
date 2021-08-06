from django.db import models
from user.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=1200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return f'/category/{self.slug}'

    def get_simple_slug(self):
        slugs = self.slug.split('-')
        return slugs[-1]

    # 복수 명칭 변경
    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    slug = models
    question = models.ManyToManyField