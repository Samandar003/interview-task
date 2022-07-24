from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'comments', views.CommentModelViewSet, basename='comments')


urlpatterns = [
    path('posts/', views.PostAPIView.as_view()),
    path('post/create/', views.PostAPIView.as_view()),
    path('comments/', views.CommentAPIView.as_view()),
    path('comments/<str:pk>/', views.CommentAPIView.as_view()),
]
