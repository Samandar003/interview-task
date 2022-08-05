from django.shortcuts import render, redirect, get_object_or_404
from main.models import Post, Comment
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class UserCreateViewSet(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [TokenAuthentication,]

    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(request):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
  
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            if post.dislikes.filter(id=request.user.id).exists():
                post.dislikes.remove(request.user)
            post.likes.add(request.user)
        return Response(PostSerializer(post).data)

    @action(detail=True, methods=['POST'])
    def dislike(self, request, *args, **kwargs):
        post = self.get_object()
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            post.dislikes.add(request.user)
        return Response(PostSerializer(post).data)

    
class CommentAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)



    
