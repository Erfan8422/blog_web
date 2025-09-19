from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path("", views.home, name='home'),
    path('/<int:pk>', views.categories, name='home'),
    path('search', views.search, name='search'),

]