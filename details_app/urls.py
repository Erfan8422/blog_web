from django.urls import path
from . import views

app_name = 'details_app'

urlpatterns = [
    path("details/<int:pk>", views.detail_app, name="details")
]