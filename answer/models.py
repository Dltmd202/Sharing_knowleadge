from django.db import models

# Create your models here.
class Answer(models.Model):
    editor = models.CharField(max_length=100)
    answer_date = models.DateTimeField()
    body = models.TextField()

    # def __str__(self):
    #     return self.editor