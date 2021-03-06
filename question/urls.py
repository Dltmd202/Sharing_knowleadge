from rest_framework.routers import DefaultRouter
from rest_framework import routers

from django.urls import path, include
from . import views



router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet())



urlpatterns = [
    path('', views.QuestionList.as_view(), name="question_main"),
    path('<int:pk>/', views.QuestionDetail.as_view(), name='res'),
    path('create_question/', views.QuestionCreate.as_view()),
    path('update_question/<int:pk>', views.QuestionUpdate.as_view(), name="question_update"),
    path('question/search/', views.QuestionUpdate.as_view(), name="question_search_base"),
    path('question/search/<str:q>/', views.QuestionSearch.as_view(), name="question_search"),
    path('question/search/<str:q>/<str:pk>', views.QuestionDetail.as_view()),
    path('report/<str:page_pk>/', views.reportView, name="report"),
    path('api-auth/', include('rest_framework.urls')),
    path('<str:slug>', views.tag_page),
]
