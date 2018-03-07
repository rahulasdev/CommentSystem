from django.urls import path
from . import views

urlpatterns=[
    path('todo',views.ListTodo.as_view()),
    path('todo/<int:pk>',views.DetailTodo.as_view()),
    path('post',views.ListPost.as_view()),
    path('post/<int:pk>',views.DetailPost.as_view()),
    path('comments',views.ListComments.as_view()),
    path('comments/<int:pk>',views.ListComments.as_view()),
]
