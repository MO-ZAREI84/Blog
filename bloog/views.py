from django.shortcuts import render
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
    try:
        posts=Post.published.get(id=id)  
    except:
        raise Http404("page is not found")
    context={ 
        'post':post,
    }
    return render(request,'blog/postdetail.html',context)