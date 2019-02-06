from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostsSerializer


class ListPostsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
