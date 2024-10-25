from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from .forms import*
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery

# Create your views here.

def index(request):
    return render(request,'blog/index.html')
def post_search(request):
    query = None
    result = []
    
    # بررسی اینکه آیا 'query' در request.GET وجود دارد
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        
        if form.is_valid():
            query = form.cleaned_data['query']
            search_query = SearchQuery(query)
            # جستجو در عنوان‌های پست
            result = Post.published.annotate(search=SearchVector('title','description')).filter(search=search_query
            )
            # result = Post.published.filter(Q(title__icontains=query)& Q(description__icontains=query))->and 
            # result = Post.published.filter(Q(title__icontains=query) ^ Q(description__icontains=query))->xor
    
    context = {
        'query': query,
        'result': result,
    }
    
    return render(request, 'blog/search.html', context)
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

def PostDetail(request,pk):
    post=get_object_or_404(Post,id=pk,status=Post.Status.PUBLISHED)
    form=CommentForm()
    comments=post.comments.filter(active=True)
    context={ 
        'post':post,
        'form':form,
        'comments':comments,
    }
    return render(request,'blog/detail.html',context)
# class PostDetailView(DetailView):
#     model=Post
#     context_object_name = "post"
#     template_name="blog/detail.html"

def ticketview(request):
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ticket_obj = Ticket(
                message=cd['message'],
                name=cd['name'],
                email=cd['email'],
                phone=cd['phone'],
                subjects=cd['subjects']  # تغییر 'subject' به 'subjects' مطابق با نام فیلد
            )
            ticket_obj.save()  # افزودن () به save
            return redirect('blog:index')  # اضافه کردن return برای redirect
    else:  # از GET یا دیگر روش‌ها
        form = TicketForm()  # باید به صورت TicketForm() ایجاد شود

    return render(request, 'forms/ticket.html', {'form': form})
 
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = None
    form = CommentForm(data=request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post  # تنظیم ارتباط بین کامنت و پست
        comment.save()
    
    context = {
        'post': post,
        'form': form,
        'comment': comment
    }
    
    return render(request, 'forms/comment.html', context)
def Profile(request):
    user=request.user
    posts= Post.published.filter(author=user)
    context={
        'user':user,
        'posts':posts,
    }
    return render(request,'blog/profile.html',context)
def Createpost(request):
    if request.method == POST:
        form=CreatePostForm(request.POST,request.FILES)
        if form_is.valid():
            post=form.save(commit=False)
            post.author=request.user
            post.images.add(request)
    context={
        
    }
    return render(request,'Createpost',context)