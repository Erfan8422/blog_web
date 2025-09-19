from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_app.urls")),
    path("", include("blog_app.urls")),
    path("", include("details_app.urls")),
    path("", include("contact_app.urls")),
    path("", include("login_app.urls")),
    path('api/token/', obtain_auth_token),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

