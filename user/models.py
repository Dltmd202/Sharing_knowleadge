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
    chosen_count = models.PositiveIntegerField(default=0)
    answer_count = models.PositiveIntegerField(default=0)

    REQUIRED_FIELDS = []

    # question의 ques_point 문자열 호출용
    def left_ques(self):
        return self.ques_point

    def left_ans_point(self):
        return self.answer_point

    def get_chosen_rate(self):
        return str(self.chosen_count / self.answer_count * 100)[:5]


''' 신고 사유 목록(임시)
    - 욕설/비하
    - 음란물/불건전한 만남 및 대화
    - 상업적 광고 및 판매
    - 유출/사칭/사기
    - 낚시/놀람/도배
'''
class Report_Class(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name



class Report(models.Model):
    desc = models.CharField(max_length=2000, null=False, blank=False)
    report_class = models.ForeignKey(Report_Class, null=False, on_delete=models.CASCADE)
    report_user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.report_class.name + "(신고자: " + self.report_user.username + ")"

class Report_Answer(Report):
    report_answer = models.ForeignKey("answer.Answer", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.report_answer.answer_title + " - " + super(Report_Answer, self).__str__()

class Report_Question(Report):
    report_question = models.ForeignKey("question.Question", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.report_question.ques_title + " - " + super(Report_Question, self).__str__()