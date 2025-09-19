from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, ArticleViewSet, CommentViewSet

app_name = 'blog_app'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("blog", views.ArticleList.as_view(), name="blog"),
    path('category/<int:pk>', views.categories, name='category'),
    path('search', views.search, name='search'),
    path('api/', include(router.urls)),
]