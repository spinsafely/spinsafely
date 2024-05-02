from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("casino/<slug:slug>", views.CasinoView.as_view(), name="casino"),
    path("accounts/login", auth_views.LoginView.as_view(template_name="casinoaffiliate_app/login.html"), name='login'),
    path("accounts/register", views.signup, name="register"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="casinoaffiliate_app/robots.txt", content_type="text/plain"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
