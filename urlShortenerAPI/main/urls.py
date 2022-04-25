from django.urls import path
from .views import URLShortenerApiView, url_redirect
urlpatterns = [
    path('api', URLShortenerApiView.as_view()),
    path("<str:slugs>", url_redirect, name="redirect")
]