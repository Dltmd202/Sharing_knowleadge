from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('answer/', include('answer.urls')),
    path('category/', include('category.urls')),
    path('company/', include('company.urls')),
    path('question/', include('question.urls')),
    path('university/', include('university.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)