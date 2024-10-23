from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse


#Manager
class publishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):
    # STATUS_CHOISES[
    #    ( 'DF' ,'DRAFT'),
    #    ('PB', 'PUBLISHED'),
    #    ('RG' , 'REGECTED'),
    # ]
    class Status(models.TextChoices):
        DRAFT='DR','DRAFT'
        PUBLISHED='PB','PUBLISHED'
        REGECTED='RG','REGECTED'


    title = models.CharField(max_length=20,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=100,verbose_name='اسلاگ')
    # CHOISEFIELD
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT,verbose_name='وضعیت')
    # relations
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_post",verbose_name='نویسنده')
    #date
    publish = jmodels.jDateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name='ناریخ تولید')
    update = jmodels.jDateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')

    # objects = models.Manager()
    objects = models.Manager()
    published = publishedManager()
    reading_time=models.PositiveIntegerField(verbose_name='زمان مطالعه',default='14')

    class Meta:
        ordering = ['-publish']
        indexes=[
            models.Index(fields=['-publish'])

        ]
        verbose_name_plural="پست ها"

    

    #over_ridemkk
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:PostDetail',args=[self.id])


class Ticket(models.Model):
    message=models.TextField(verbose_name='پیام')
    name=models.CharField(max_length=250,verbose_name=' نام')
    email=models.EmailField(verbose_name='ایمیل')
    phone=models.CharField(max_length=11,verbose_name='شماره')
    subjects=models.CharField(max_length=240,verbose_name='موضوع')

    class Meta:
        verbose_name='تیکت'
        verbose_name_plural='تیکتها'

    def __str__(self):
        return self.subjects
class Comment(models.Model):
    post=models.ForeignKey(Post,verbose_name='پست',on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=250,verbose_name=' نام')
    body=models.TextField(verbose_name='پیام')
    publish = models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    create = models.DateTimeField(auto_now_add=True,verbose_name='ناریخ تولید')
    active=models.BooleanField(default=True, verbose_name=' فعالیت')
    
    class Meta:
        verbose_name='کامنت '
        verbose_name_plural = ' کامنت ها'

    def __str__(self):
        return self.name
class ImageField(models.Model):
    post=models.ForeignKey(Post,verbose_name='تصویر',on_delete=models.CASCADE,related_name='images')
    image_file=models.ImageField(upload_to="post_images/")
    title = models.CharField(max_length=20,verbose_name='عنوان',null=True,blank=True)
    description = models.TextField(verbose_name='توضیحات',null=True,blank=True)
    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name='ناریخ تولید')