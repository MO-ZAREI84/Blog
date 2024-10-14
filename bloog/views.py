from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from .forms import*
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    return render(request,'blog/index.html')

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
