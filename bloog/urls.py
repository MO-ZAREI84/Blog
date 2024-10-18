from django.contrib import admin
from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
  path('',index,name='index'),
  path('posts/',PostListView.as_view(),name='PostList'),
  # path('Posts/',PostListView.as_view(),name='Post_List'),
  # path('Posts/<pk>',PostDetailView.as_view(),name='PostDetail'),
  path('Posts/<pk>',PostDetail,name='PostDetail'),
  path('forms/',ticketview,name='ticket_forms'),
  path('Posts/<post_id>/comment',post_comment,name='post_comment'),
  path('search/', post_search, name='post_search'),

  # path('Posts/<pk>',views.PostDetailView.as_view(),name='Post_Detail'),
]