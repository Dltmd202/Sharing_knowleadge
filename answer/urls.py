from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnswerList.as_view()),
    path('<int:pk>/', views.AnswerDetail.as_view(), name='res'),
    path('<int:pk>/new_answer', views.new_answer),
    path('<int:pk>/vote/<int:answer_pk>/', views.vote_answer, name="vote_answer"),
    path('<int:pk>/select/<int:answer_pk>', views.select_answer, name="select_answer"),
    path('edit_answer/', views.AnswerEdit.as_view()),
    path('answer/search/<str:q>/', views.AnswerSearch.as_view()),
    path('answer/search/<str:q>/<str:pk>', views.AnswerDetail.as_view()),
]
