from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views


router = routers.DefaultRouter()
# router.register(r'comments', views.CommentModelViewSet, basename='comments')
router.register('posts', views.PostModelViewSet, basename='post')

urlpatterns = [
    path('token-auth/', auth_views.obtain_auth_token)
]

urlpatterns += router.urls
