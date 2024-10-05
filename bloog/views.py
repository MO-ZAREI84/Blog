from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post

# Create your views here.

def index(request):
    return HttpResponse("heloo")

def PostList(request):
    posts=Post.published.all()
    context={ 
        'posts':posts,
    }
    return render(request,'blog/list.html',context)

def PostDetail(request,id):
    post=get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    context={ 
        'post':post
    }
    return render(request,'blog/detail.html',context)