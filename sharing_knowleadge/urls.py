from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
from question.views import QuestionViewSet

router = DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('answer/', include('answer.urls')),
    path('comment/', include('comment.urls')),
    path('category/', include('category.urls')),
    path('company/', include('company.urls')),
    path('university/', include('university.urls')),
    path('user/', include('user.urls')),
    path('question/', include('question.urls')),
    path('viewset/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)