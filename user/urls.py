from django.contrib.auth.models import User
from django.urls import path
from . import views
from .forms import UserCreationForm1, UserCreationForm2

urlpatterns = [
    path('register/', views.UserRegisterView.as_view([UserCreationForm1, UserCreationForm2]), 
        name="register"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('mypage/', views.mypageView, name="mypage"),
    path('edit/', views.userEditPageView, name="edit"),
    path('spec/', views.specView, name="spec"),
    path('exchange/', views.exchangeView, name="exchange"),
    path('credits/', views.show_me_the_money, name="credits")
]

