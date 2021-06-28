from answer.views import create, edit, home, new
from django.contrib import admin
from django.urls import path
from answer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name="home"),
    path('new/', new,name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit")
]
