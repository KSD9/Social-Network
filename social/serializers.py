from rest_framework import serializers
from django.contrib.auth.models import User, AnonymousUser
from social.models import Post, UserProfile , Like



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            '__all__'
                  )


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            '__all__'
        )


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "password")


class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255)