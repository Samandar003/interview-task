from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUp(generic.CreateView):
    model = User
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    template_name = 'register.html'

class CustomLoginView(LoginView):
  template_name = 'login.html'
  fields = '__all__'
  redirect_authenticated_user = True
  def get_success_url(self) -> str:
      return reverse_lazy('index') 

def logoutPage(request):
    logout(request)
    return redirect('login')

class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class Post_View(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__id=self.kwargs['pk'])
        context['comments_count'] = len(context['comments'])
        return context

class Post_Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'post/post_edit.html'
    context_object_name = 'post'
    fields = ['title', 'text']
    success_url = reverse_lazy('/')
    model = Post

    def test_func(self):
        post = self.get_object()
        return True if post.user == self.request.user else False

class Create_post(CreateView, LoginRequiredMixin):
    template_name = 'post/create_post.html'
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super(Create_post, self).form_valid(form)

class Create_Comment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/create_comment.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super(Create_Comment, self).form_valid(form)

class Comment_Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/comment_edit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super(Comment_Edit, self).form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return True if comment.user == self.request.user else False

class Post_Delete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'post/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('index')

    def test_func(self):
        post = self.get_object()
        return True if post.user == self.request.user else False


class Comment_Delete(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = Comment
    template_name = 'comment/comment_delete.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('index')

    def test_func(self):
        comment = self.get_object()
        return True if comment.user == self.request.user else False

