from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from django.urls import path
# from api.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()
# router.register(r'comments', views.CommentModelViewSet, basename='comments')
router.register('posts', views.PostModelViewSet, basename='post')


urlpatterns = [
    path('token-auth/', auth_views.obtain_auth_token),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserCreateViewSet.as_view()),
]

urlpatterns += router.urls
