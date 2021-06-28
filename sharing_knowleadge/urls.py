from answer.views import create, edit, home, new
from django.contrib import admin
from django.urls import path, include
from answer.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', include('question.urls')),
    path('answer/', include('answer.urls')),
    path('category/', include('category.urls')),
    path('user/', include('user.urls')),
    path('university', include('university.urls')),
    path('company', include('company.urls')),
    path('', home , name="home"),
    path('new/', new,name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)