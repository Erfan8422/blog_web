from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog_app.models import Article, Category, Comment
import logging


# Create your views here.


def home(request):
    articles = Article.objects.all().order_by('-blog_views')[:3]
    articles_banner = Article.objects.all()
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request, "index.html", context={'articles': articles, 'cats': categories, 'articles_banner': articles_banner, 'recent_articles': recent_articles})

def categories(request, pk=None):
    articles_banner = Article.objects.all()
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all().order_by('-blog_views')
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request, 'index.html', context={'articles': articles, 'cats': categories, 'articles_banner': articles_banner, 'recent_articles': recent_articles})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(tittle__icontains=q)
    return render(request, 'blog.html', context={'articles': articles})
