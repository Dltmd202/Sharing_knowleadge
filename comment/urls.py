from django.urls import path
from comment import views

urlpatterns = [
    path('', views.CommentDetail.as_view()),
    # path('<int:pk>/', views.CommentDetail.as_view(), name='res'),
    path('<int:pk>/new_comment', views.new_comment),
    path('edit_comment/', views.CommentEdit.as_view()),
]
