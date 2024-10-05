from django.contrib import admin
from django.urls import path
from .views import PostDetail,PostList,index

app_name='blog'

urlpatterns = [
  path('',index,name='index'),
  path('posts/',PostList,name='PostList'),
  path('Posts/<int:id>',PostDetail,name='PostDetail')
]