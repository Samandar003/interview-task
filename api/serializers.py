from rest_framework import serializers
from main.models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
    
    # def __call__(self, serializer_field):
    #     return serializer_field.context['request'].user

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=1000)
    user = UserSerializer()

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    text = serializers.CharField(max_length=1000)
    user = UserSerializer()



