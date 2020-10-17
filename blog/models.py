from django.db import models
from django.utils import timezone
from django.urls import  reverse, reverse_lazy
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()
class Post(models.Model):
    author          = models.ForeignKey(User,on_delete=models.CASCADE)
    title           = models.CharField(max_length=200)
    content         = models.TextField(max_length=3000)
    created_date    = models.DateTimeField(auto_now_add=True)
    edited_date     = models.DateTimeField(blank=True, null=True)
    post_views      = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def viewed(self):
        self.post_views +=1
        self.save() 

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.pk})



class Comment(models.Model):
    post            = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author          = models.CharField(max_length=200)
    content         = models.TextField(max_length=500)
    created_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.pk})
