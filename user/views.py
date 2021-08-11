from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from formtools.wizard.views import SessionWizardView
from .models import CustomUser
from .forms import UserCreationForm1, UserCreationForm2, \
    UserPasswordEditForm, CustomLoginForm, PointExchangeForm
from itertools import chain
import datetime

# Company
from company.forms import CompanyForm
# University
from university.forms import UniversityForm


# 한 페이지에서 여러 폼을 다루기 위해서 formtools를 설치해서 Session Wizard View를 특별히 사용합니다
# pip install django-formtools
class UserRegisterView(SessionWizardView):
    template_name = "user/register.html"  # 회원가입 템플릿 위치
    form_list = [UserCreationForm1, UserCreationForm2]  # 사용할 폼 종류

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
        user.set_password(password)  # 비밀번호를 해쉬값으로 저장
        user.save()

        return render(self.request, 'user/done.html', {'form': form_data, 'count': len(form_list)})


def loginView(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            stayLoggedIn = form.cleaned_data.get("stay_logged_in")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                if stayLoggedIn:
                    request.session.set_expiry(100000)
                return redirect('/')
    else:
        form = CustomLoginForm()

    return render(request, 'user/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('/')


def mypageView(request):
    if request.user.is_authenticated:
        user = request.user
        answer = user.answer_set.all()
        question = user.question_set.all()
        university = user.university_set.all()
        company = user.company_set.all()
        uni_len = len(university)
        comp_len = len(company)
        total_len = 6
        return render(request, 'user/mypage.html', 
            {
                'answer_list': answer,
                'question_list': question,
                'university': university[:total_len],
                'company': company[:(total_len - uni_len)]
            })
    else:
        return HttpResponseForbidden()


def userEditPageView(request):
    if request.user.is_authenticated:
        user = request.user
        success = None

        form1 = UserPasswordEditForm()
        form2 = UserCreationForm2()
        form2.initial['user_desc'] = user.user_desc
        form2.initial['email'] = user.email
        birth_date = user.birth_date
        form2.initial['birth_year'] = birth_date.year
        form2.initial['birth_month'] = birth_date.month
        form2.initial['birth_day'] = birth_date.day

        if request.method == 'POST':
            data = request.POST
            if data.get("password_change"):
                form1 = UserPasswordEditForm(
                    data={'password': data['password'], 'password_again': data['password_again']}
                )
                if form1.is_valid():
                    cleaned_data = form1.cleaned_data
                    user.set_password(cleaned_data['password'])
                    user.save()
                    success = True
            elif data.get("other_change"):
                form2 = UserCreationForm2(
                    data={'user_desc': data['user_desc'], 'email': data['email'],
                          'birth_year': data['birth_year'], 'birth_month': data['birth_month'],
                          'birth_day': data['birth_day']}
                )
                if form2.is_valid():
                    cleaned_data = form2.cleaned_data
                    user.user_desc = cleaned_data['user_desc']
                    user.email = cleaned_data['email']
                    dateString = cleaned_data['birth_year'] + "-" + \
                                 cleaned_data['birth_month'] + "-" + cleaned_data['birth_day']
                    birth_date = datetime.datetime.strptime(dateString, "%Y-%m-%d")
                    user.save()
                    success = True

        return render(request, 'user/user_edit.html', {'form1': form1, 'form2': form2, 'success': success})
    else:
        return HttpResponseForbidden()


def specView(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            data = request.POST
            type = data['form-type']
            if type == "university":
                pk = data['primary-key']
                delete_uni = get_object_or_404(user.university_set, pk=pk)
                delete_uni.delete()
            elif type == "company":
                pk = data['primary-key']
                delete_comp = get_object_or_404(user.company_set, pk=pk)
                delete_comp.delete()
            # new_company
            elif type == 'new_company':
                company_create_form = CompanyForm(request.POST)
                if request.user.is_authenticated:
                    create_company = company_create_form.save(commit=False)
                    create_company.user_id = request.user
                    create_company.save()
            # new_university
            elif type == 'new_university':
                univ_create_form = UniversityForm(request.POST)
                if request.user.is_authenticated:
                    create_university = univ_create_form.save(commit=False)
                    create_university.user_id = request.user
                    create_university.save()
            return redirect('spec')
        new_company = CompanyForm()
        new_university = UniversityForm()
        university = user.university_set.all()
        company = user.company_set.all()
        return render(request, 'user/spec.html', {
            'university': university, 'company': company,
            'new_university': new_university,
            'new_company': new_company,
        })
    else:
        return HttpResponseForbidden()


def exchangeView(request):
    if request.user.is_authenticated:
        user = request.user
        success = None
        form = PointExchangeForm()
        if request.method == 'POST':
            form = PointExchangeForm(request.POST, request=request)
            if form.is_valid():
                point_type = form.cleaned_data['point_type']
                point_amount = form.cleaned_data['point_amount']
                if point_type == "question":
                    user.ques_point -= point_amount
                else:
                    user.answer_point -= point_amount
                user.account += point_amount
                user.save()
                success = point_amount

        return render(request, 'user/exchange.html', {'form':form, 'success':success})
    else:
        return HttpResponseForbidden()