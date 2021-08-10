from django.db import models
from user.models import CustomUser
from category.models import Category
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, allow_unicode=True, unique=True)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        return f'/question/{self.slug}'


# User 모델 완성 후 수정할 것
class Question(models.Model, HitCountMixin):
    ques_title = models.CharField(max_length=30)
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    ques_desc = models.TextField()
    ques_point = models.IntegerField(null=True, blank=True)
    head_img = models.FileField(upload_to='question/images/%Y/%m/%d/', blank=True)
    who_chosen = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name='who_chosen')
    vote_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, null=True, blank=False)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def __str__(self):
        return str(self.pk) + ': ' + self.ques_title

    def title_brief(self):
        if len(self.ques_title) < 15:
            return self.ques_title
        return self.ques_title[:15] + '...'

    def brief(self):
        if len(self.ques_desc) < 20:
            return self.ques_desc
        return self.ques_desc[:20] + '...'

    def answer_count(self):
        return self.answer_count()

    def get_absolute_url(self):
        return f'/question/{self.pk}/'


