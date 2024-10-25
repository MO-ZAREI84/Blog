from django.contrib import admin
from .models  import *


# Register your models here.

admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title="پنل "
admin.sites.AdminSite.site_index="پنل مدیریت"
class ImageInlineAdmin(admin.TabularInline):
    model=ImageField
    extra=1
    readonly_fields=('id','title')
class commentInline(admin.StackedInline):
    model=Comment
    extra=1
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish','status']
    ordering = ['title']
    list_filter = ['status','author','publish']
    search_fields = ['title','description']
    prepopulated_fields={ "slug" : ['title'] }
    list_editable=['status']
    list_display_links=['title','author']
    inlines= [ImageInlineAdmin,commentInline]

@admin.register(Ticket)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','email',]
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','create','active']
    list_filter = ['active']
    search_fields=['body','name']
    list_editable=['active']
@admin.register(ImageField)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post','title','create']
