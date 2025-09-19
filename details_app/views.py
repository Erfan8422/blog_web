from django.shortcuts import render
from blog_app.models import Article, Comment

# Create your views here.


def detail_app(request, pk=None):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    article.blog_views = article.blog_views + 1
    article.save()
    return render(request, "post-details.html", context={'article': article})