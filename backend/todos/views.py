from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    queryset= models.Todo.objects.all()
    serializer_class=serializers.TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Todo.objects.all()
    serializer_class=serializers.TodoSerializers

class ListPost(generics.ListCreateAPIView):
    queryset= models.Post.objects.all()
    serializer_class=serializers.PostsSerializers


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Post.objects.all()
    serializer_class=serializers.PostsSerializers

class ListComments(generics.ListCreateAPIView):
    queryset= models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers


class DetailComments(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers
