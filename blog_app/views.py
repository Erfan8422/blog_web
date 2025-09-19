from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic.base import TemplateView


# Create your views here.


def blog_app(request):
    articles = Article.objects.all().order_by('-blog_views')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    articles_list = paginator.get_page(page_number)
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request, "blog.html", context={'articles': articles_list, 'cats': categories, 'recent_articles': recent_articles})


def categories(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all().order_by('-blog_views')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    articles_list = paginator.get_page(page_number)
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request, 'blog.html', context={'articles': articles_list, 'cats': categories, 'recent_articles': recent_articles})

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(tittle__icontains=q)
    return render(request, 'blog.html', context={'articles': articles})






class ArticleList(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
