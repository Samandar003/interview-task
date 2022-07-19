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

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def post_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post__id=pk)
    comments_count = len(comments)
    context = {'post':post, 'comments':comments, 'comments_count':comments_count}
    return render(request, 'post_view.html', context)

@login_required(login_url='login')
def post_edit(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if request.method == 'POST':
            post.title = request.POST['title']
            post.text = request.POST['text']
            post.save()
            return redirect('/')
    return render(request, 'post/post_edit.html', {'post':post})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        Post.objects.create(title=request.POST.get('title'), text=request.POST['text'], user=request.user)
        return redirect('index')
    return render(request, 'post/create_post.html')


@login_required(login_url='login')
def create_comment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        text = request.POST['text']
        user = User.objects.get(pk=request.user.pk)
        comment = Comment.objects.create(post=post, text=text, user=user)
        comment.save()
        return redirect('index')
    return render(request, 'comment/create_comment.html')

@login_required(login_url='login')
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.text = request.POST['text']
        comment.save()
        return redirect('/')
    return render(request, 'comment/comment_edit.html', {'comment':comment})


# class PostCreateView(LoginRequiredMixin, CreateView):
#   model = Post
#   fields = ['title', 'text']
#   template_name = 'post/post_create.html'  
#   def form_valid(self, form):
#     form.instance.author = self.request.user
#     return super().form_valid(form)

