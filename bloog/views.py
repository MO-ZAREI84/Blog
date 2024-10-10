from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    return HttpResponse("heloo")

# def PostList(request):
#     posts=Post.published.all()
#     paginator=Paginator(posts,2)
#     number_pages=request.GET.get('page',1)
#     try:
#         posts=paginator.page(number_pages)
#     except EmptyPage:
#         posts=paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts=paginator.page(1)
#     context={
#         'posts':posts,
#     }
#     return render(request,'blog/list.html',context)

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = "blog/list.html"

# def PostDetail(request,id):
#     post=get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
#     context={ 
#         'post':post
#     }
#     return render(request,'blog/detail.html',context)
class PostDetailView(DetailView):
    model=Post
    context_object_name = "post"
    template_name="blog/detail.html"