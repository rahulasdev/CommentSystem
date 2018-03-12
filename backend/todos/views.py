from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics
from . import models
from . import serializers
from rest_framework import permissions
from .permissions import IsOwner

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class =serializers.UserSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset= models.Todo.objects.all()
    serializer_class=serializers.TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Todo.objects.all()
    serializer_class=serializers.TodoSerializers

class ListPost(generics.ListCreateAPIView):
    queryset= models.Post.objects.all()
    serializer_class=serializers.PostsSerializers
    permission_classes=(permissions.IsAuthenticated,IsOwner)
    def perform_create(self , serializer):
        serializer.save(created_by=self.request.user)


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Post.objects.all()
    serializer_class=serializers.PostsSerializers

class ListComments(generics.ListCreateAPIView):
    queryset= models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers

    def perform_create(self , serializer):
        serializer.save(created_by=self.request.user)


class DetailComments(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Comments.objects.all()
    serializer_class=serializers.CommentsSerializers
