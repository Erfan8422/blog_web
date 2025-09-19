from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    tittle = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category, related_name="articles")
    tittle = models.CharField(max_length=50, null=True)
    body = models.TextField(max_length=100000, null=True)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    blog_views = models.IntegerField(default=0)

    # class Meta:
    #     ordering = ('-updated', '-created',)

    def __str__(self):
        return self.tittle


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)