from django.urls import path

from .views import (
    ArticleLCView,
    ArticleRUDView,
)


urlpatterns = [
    path('article-lc/', ArticleLCView.as_view(), name='article-lc'),
    path('article-rud/<slug:slug>/', ArticleRUDView.as_view(), name='article-rud'),
]
