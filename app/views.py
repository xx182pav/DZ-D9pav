from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer, PostSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Author, Post, Category


class AuthorList(generics.ListCreateAPIView):  
    queryset = Author.objects.all()  
    serializer_class = AuthorSerializer


class RetrieveAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostList(generics.ListCreateAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer
    # lookup_field = ['id']

class RetrievePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetrieveCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'










   


    # def post(self, request, *args, **kwargs):  
    #     ...

    


# class PostDetail(generics.RetrieveAPIView):  
#     queryset = Post.objects.all()  
#     serializer_class = PostSerializer






    
