from typing import Text
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from .models import CustomUser


class UserCreationForm1(forms.ModelForm): # 회원가입 첫번째 페이지 폼(아이디, 비번)
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"비밀번호 재입력"})
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={"placeholder":"아이디 입력"}),
            "password": PasswordInput(attrs={"placeholder":"비밀번호 입력"})
        }
    
    def clean(self): # 비밀번호 재입력 검사 메소드
        cleaned_data = super(UserCreationForm1, self).clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")

        if password != password_again:
            raise forms.ValidationError("패스워드가 서로 일치하지 않습니다!")

        return cleaned_data


class UserCreationForm2(forms.ModelForm): # 회원가입 두번째 페이지 폼(닉네임, 이메일, 생년월일)
    class Meta:
        model = CustomUser
        fields = ['user_desc', 'birth_date', 'email']
        widgets = {
            "user_desc": TextInput(attrs={"placeholder":"닉네임 입력"}),
            "birth_date": TextInput(attrs={"placeholder":"생년월일 입력", "type":"date"}),
            "email": TextInput(attrs={"placeholder":"이메일 입력"}),
        }

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    classValue = "form-control"
    styleValue = "background-color: #F1F9FF; height: 3rem;"
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"아이디 입력", "class":classValue, "style":styleValue
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"비밀번호 입력", "class":classValue, "style":styleValue,
        "id":"password-input"
    }))