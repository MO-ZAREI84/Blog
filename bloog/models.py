from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


    title = models.CharField(max_length=20)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    # CHOISEFIELD
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    # relations
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_post")
    #date
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = publishedManager()

    class Meta:
        ordering = ['-publish']
        indexes=[
            models.Index(fields=['-publish'])

        ]


    #over_ridemkk
    def __str__(self):
        return self.title

