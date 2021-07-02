from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from formtools.wizard.views import SessionWizardView
from .models import CustomUser
from .forms import UserCreationForm1, UserCreationForm2, CustomLoginForm
from company.models import Company
from university.models import University
import datetime


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
        birth_year = form_data["birth_year"]
        birth_month = form_data["birth_month"]
        birth_day = form_data["birth_day"]
        email = form_data["email"]

        dateString = birth_year + "-" + birth_month + "-" + birth_day
        birth_date = datetime.datetime.strptime(dateString, "%Y-%m-%d")
        user = CustomUser(username=username, password=password, user_desc=user_desc, 
            birth_date=birth_date, email=email)
        user.set_password(password) # 비밀번호를 해쉬값으로 저장
        user.save()
                
        return render(self.request, 'user/done.html', {'form':form_data, 'count':len(form_list)})


def loginView(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else: 
        form = CustomLoginForm()
    return render(request, 'user/login.html', {'form':form})


def logoutView(request):
    logout(request)
    return redirect('/')


def mypageView(request):
    if request.user.is_authenticated:
        return render(request, 'user/mypage.html')
    else:
        return HttpResponseForbidden()


def specView(request):
    if request.user.is_authenticated:
        current_user = request.user
        university_list = University.objects.filter(user_id=current_user)
        company_list = Company.objects.filter(user_id=current_user)
        return render(request, 'user/spec_page.html',
                      {
                          'university_list': university_list,
                          'company_list': company_list,
                      })
    else:
        return HttpResponseForbidden()