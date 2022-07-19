from django import forms
from .models import Post, Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user']


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']




