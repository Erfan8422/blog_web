from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path("login", views.login_app, name='login'),
    path("signin", views.user_signup, name='signin'),
    path("logout", views.logout_app, name='logout'),
]