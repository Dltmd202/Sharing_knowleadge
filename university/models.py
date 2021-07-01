from django.db import models
from user.models import CustomUser

class University(models.Model):
    # 유저 이름, int타입
    user_id = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    # 대학 이름, 학년, 전공, 입학년도, 졸업년도, 재학중인지 체크박스
    uni_name = models.CharField(max_length=50)
    uni_degree = models.CharField(max_length=50)
    uni_major = models.CharField(max_length=50)
    
    # DateField는 datetime.date 인스턴스인 날짜 데이터를 저장하는 필드. 달력 위젯과 오늘 날짜 입력 기능 기본제공
    # HTML 위젯 : TextInput
    enter_date = models.DateField()
    grad_date = models.DateField(null=True, blank = True)
    
    # HTML 위젯 : CheckboxInput
    is_attending = models.BooleanField()

# def __str__(self):
#     return self.uni_name
# call method시, db에서 user_id로 볼 수 있게함