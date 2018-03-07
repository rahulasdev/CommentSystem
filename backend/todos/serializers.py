from rest_framework import serializers
from . import models

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'title',
        'description',
        )
        model= models.Todo

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'post_comment',
        'created_by',
        'created_at'
        )
        model=models.Post

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'post',
        'comments',
        'created_at',
        'created_by',
        )
        model=models.Comments
