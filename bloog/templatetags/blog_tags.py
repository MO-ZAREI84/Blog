from django import template
from ..models import Post,Comment
from django.db.models import Count
from markdown import markdown
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag()
def total_posts():
    return Post.published.count()
@register.simple_tag()
def total_comment():
    return Comment.objects.filter(active=True).count()


@register.simple_tag()
def last_post():
    return Post.published.last().publish

@register.simple_tag()
def popular_post(count=3):
    p=Post.published.annotate(comment_count=Count('comments')).order_by('-comment_count')[:count]
    
    return p
@register.filter()
def to_markdown(text):
    return  mark_safe (markdown(text))