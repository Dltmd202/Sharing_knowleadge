from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.UnivCreate.as_view(), name="new_univ"),
]