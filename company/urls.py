from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.CompCreate.as_view(), name = "new"),
]