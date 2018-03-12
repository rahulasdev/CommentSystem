from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id',
        'username',
        )
        model = User

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'title',
        'description',
        )
        model= models.Todo

class CommentsSerializers(serializers.ModelSerializer):
    created_by=serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        fields=(
        'id',
        #'post',
        'comments',
        'created_at',
        'created_by',
        )
        read_only_fields=('created_at','id')
        model=models.Comments

class PostsSerializers(serializers.ModelSerializer):
    created_by=serializers.ReadOnlyField(source='created_by.username')
    comments = CommentsSerializers(many=True,read_only=True)
    class Meta:
        fields=(
        'id',
        'post_comment',
        'created_by',
        'created_at',
        'comments',
        )
        read_only_fields=('created_at','id')
        model=models.Post
