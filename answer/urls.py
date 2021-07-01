from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnswerList.as_view()),
    path('<int:pk>/', views.AnswerDetail.as_view(), name='res'),
    path('new_answer/', views.AnswerNew.as_view()),
    path('edit_answer/', views.AnswerEdit.as_view()),
    path('answer/search/<str:q>/', views.AnswerSearch.as_view()),
    path('answer/search/<str:q>/<str:pk>', views.AnswerDetail.as_view()),
]
