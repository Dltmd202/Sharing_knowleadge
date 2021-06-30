from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionList.as_view(), name="question"),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='res'),
    path('create_question/', views.QuestionCreate.as_view()),
    path('update_question/', views.QuestionUpdate.as_view()),
    path('question/search/<str:q>/', views.QuestionSearch.as_view()),
    path('question/search/<str:q>/<str:pk>', views.QuestionDetail.as_view()),
]