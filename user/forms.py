from typing import Text
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from .models import CustomUser
import datetime

classValue = "form-control"
styleValue = "background-color: #F1F9FF; height: 3rem;"


class UserCreationForm1(forms.ModelForm):  # 회원가입 첫번째 페이지 폼(아이디, 비번)
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 재입력", "class": classValue + " password-input", "style": styleValue
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                "placeholder": "아이디 입력", "class": classValue, "style": styleValue
            }),
            "password": PasswordInput(attrs={
                "placeholder": "비밀번호 입력", "class": classValue + " password-input", "style": styleValue
            })
        }

    def clean(self):  # 비밀번호 재입력 검사 메소드
        cleaned_data = super(UserCreationForm1, self).clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")

        if password != password_again:
            raise forms.ValidationError("패스워드가 서로 일치하지 않습니다!")

        return cleaned_data


class UserCreationForm2(forms.ModelForm):  # 회원가입 두번째 페이지 폼(닉네임, 이메일, 생년월일)
    MONTH_CHOICE = ((i, '{}월'.format(i)) for i in range(1, 13))
    DAY_CHOICE = ((i, '{}일'.format(i)) for i in range(1, 32))

    birth_year = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "생년", "class": classValue, "style": styleValue
        })
    )
    birth_month = forms.CharField(
        widget=forms.Select(choices=MONTH_CHOICE, attrs={
            "placeholder": "생월", "class": classValue + " form-select", "style": styleValue
        })
    )
    birth_day = forms.CharField(
        widget=forms.Select(choices=DAY_CHOICE, attrs={
            "placeholder": "생일", "class": classValue + " form-select", "style": styleValue
        })
    )

    class Meta:
        model = CustomUser
        fields = ['user_desc', 'email']

        widgets = {
            "user_desc": TextInput(attrs={
                "placeholder": "닉네임 입력", "class": classValue, "style": styleValue
            }),
            "email": TextInput(attrs={
                "placeholder": "이메일 입력", "class": classValue, "style": styleValue
            }),
        }

    def clean(self):
        cleaned_data = super(UserCreationForm2, self).clean()
        try:
            year = cleaned_data.get("birth_year")
            intYear = int(year)
            if intYear < 1950 or intYear > int(datetime.datetime.today().year):
                raise AssertionError
            month = cleaned_data.get("birth_month")
            day = cleaned_data.get("birth_day")
            dateString = year + "-" + month + "-" + day
            datetime.datetime.strptime(dateString, "%Y-%m-%d")
        except ValueError:
            raise forms.ValidationError("날짜 형식이 맞지 않습니다.")
        except TypeError:
            raise forms.ValidationError("연도 형식이 맞지 않습니다.")
        except AssertionError:
            raise forms.ValidationError("연도 범위를 초과했습니다.")

        return cleaned_data


class UserPasswordEditForm(UserCreationForm1):
    class Meta:
        model = CustomUser
        fields = ['password']
        widgets = {
            "password": PasswordInput(attrs={
                "placeholder": "비밀번호 입력", "class": classValue + " password-input", "style": styleValue
            })
        }


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "아이디 입력", "class": classValue, "style": styleValue
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "비밀번호 입력", "class": classValue + " password-input", "style": styleValue,
    }))
    stay_logged_in = forms.NullBooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "class":"form-check-input", "id":"loginCheck"
    }))




class CustomSelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        if option.get('value') == 2:
            option['attrs']['disabled'] = True
        
        return option


class PointExchangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PointExchangeForm, self).__init__(*args, **kwargs)

    CHOICES = (("", "포인트 종류 선택"), ("question", "질문 포인트"), ("answer", "답변 포인트"))
    point_type = forms.CharField(
        widget=CustomSelect(choices=CHOICES, attrs={

            "placeholder": "포인트 선택", "class":classValue+" form-select", "style":styleValue
        })
    )
    point_amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "placeholder": "환전할 포인트", "class":classValue, "style":styleValue
        })
    )

    def clean(self):
        cleaned_data = super(PointExchangeForm, self).clean()
        point_type = cleaned_data.get("point_type")
        point_amount = cleaned_data.get("point_amount")

        if point_type not in ["question", "answer"]:
            raise forms.ValidationError("포인트 종류가 맞지 않습니다.")
        try:
            if type(int(point_amount)) != type(1):
                raise ValueError
        except ValueError:
            raise forms.ValidationError("포인트 수량 형식이 맞지 않습니다.")
        if (point_type == "question" and point_amount > self.request.user.ques_point) \
            or (point_type == "answer" and point_amount > self.request.user.answer_point):
            raise forms.ValidationError("환전할 포인트가 부족합니다.")
            
        return cleaned_data

