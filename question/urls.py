from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuestionList.as_view(), name="question_main"),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='res'),
    path('create_question/', views.QuestionCreate.as_view()),
    path('update_question/', views.QuestionUpdate.as_view()),
    path('question/search/', views.QuestionUpdate.as_view(), name="question_search_base"),
    path('question/search/<str:q>/', views.QuestionSearch.as_view(), name="question_search"),
    path('question/search/<str:q>/<str:pk>', views.QuestionDetail.as_view()),
]