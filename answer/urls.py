from . import create, edit,  new
from django.contrib import admin
from django.urls import path
from . import *

urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit")
]
