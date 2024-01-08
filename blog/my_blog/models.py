from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0 , "draft"), (1, "published"))

class Post(models.Model):
    STATUS_CHOICES = STATUS
    title = models.CharField(max_length=250, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'blog_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    class Meta:
        ordering = ['-created_on']
        def __str__(self):
            return self.title
            


