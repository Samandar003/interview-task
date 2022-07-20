from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create_post/', views.Create_post.as_view(), name='create_post'),
    path('post_view/<str:pk>/', views.Post_View.as_view(), name='post_view'),
    path('create_comment/<str:pk>/', views.Create_Comment.as_view(), name='create_comment'),
    path('post_edit/<str:pk>/', views.Post_Edit.as_view(), name='post_edit'),
    path('logout/', views.logoutPage, name='logout'),
    path('comment_edit/<str:pk>/', views.Comment_Edit.as_view(), name='comment_edit'),
    path('post_delete/<str:pk>/', views.Post_Delete.as_view(), name='post_delete'),
    path('comment_delete/<str:pk>/', views.Comment_Delete.as_view(), name='comment_delete'),
]

