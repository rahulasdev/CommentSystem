from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        "A string representaion"
        return self.title
class Post(models.Model):
    post_comment=models.TextField()
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,default=1)
    comments=models.TextField()
    created_by=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
