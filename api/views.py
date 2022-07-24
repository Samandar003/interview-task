from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post, Comment
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, viewsets


class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post = PostSerializer(data=request.data)
        post.is_valid(raise_exception=True)
        # post.user = User.objects.get(user=request.user)
        post.save()
        return Response(data=post.data)
    def get_pk(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class CommentAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)

