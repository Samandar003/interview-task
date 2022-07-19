from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_view/<str:pk>/', views.post_view, name='post_view'),
    path('create_comment/<str:pk>/', views.create_comment, name='create_comment'),
    path('post_edit/<str:pk>/', views.post_edit, name='post_edit'),
    path('logout/', views.logoutPage, name='logout'),
    path('comment_edit/<str:pk>/', views.comment_edit, name='comment_edit'),
]

