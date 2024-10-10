from django.contrib import admin
from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
  path('',views.index,name='index'),
  # path('posts/',PostList,name='PostList'),
  path('Posts/',views.PostListView.as_view(),name='Post_List'),
  # path('Posts/<int:id>',PostDetail,name='PostDetail'),
  path('Posts/<pk>',views.PostDetailView.as_view(),name='Post_Detail'),
]