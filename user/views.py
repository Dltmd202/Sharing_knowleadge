from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from formtools.wizard.views import SessionWizardView
from .models import CustomUser
from .forms import UserCreationForm1, UserCreationForm2


# 한 페이지에서 여러 폼을 다루기 위해서 formtools를 설치해서 Session Wizard View를 특별히 사용합니다
# pip install django-formtools
class UserRegisterView(SessionWizardView):
    template_name = "user/register.html" # 회원가입 템플릿 위치
    form_list = [UserCreationForm1, UserCreationForm2] # 사용할 폼 종류

    # 폼 입력 완료 후 호출 메소드
    def done(self, form_list, **kwargs):

        # 받은 폼들을 이용해서 새로운 유저 생성 후 저장
        form_data = {}
        for form in form_list:
            for key, value in form.cleaned_data.items():
                form_data[key] = value
        username = form_data["username"]
        password = form_data["password"]
        user_desc = form_data["user_desc"]
        birth_date = form_data["birth_date"]
        email = form_data["email"]
        user = CustomUser(username=username, password=password, user_desc=user_desc, 
            birth_date=birth_date, email=email)
        user.save()
                
        return render(self.request, 'user/done.html')