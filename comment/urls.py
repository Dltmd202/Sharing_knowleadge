from rest_framework.routers import DefaultRouter
from django.urls import path
from comment import views

urlpatterns = [
    path('',views.CommentCreate.as_view()),
    path('<int:pk>/new_comment/', views.CommentCreate, name="new_comment"),
    path('')

]