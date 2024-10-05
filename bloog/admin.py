from django.contrib import admin
from .models  import Post


# Register your models here.

admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title="پنل "
admin.sites.AdminSite.site_index="پنل مدیریت"
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish','status']
    ordering = ['title']
    list_filter = ['status','author','publish']
    search_fields = ['title','description']
    prepopulated_fields={ "slug" : ['title'] }
    list_editable=['status']
    list_display_links=['title','author']