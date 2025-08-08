from django.urls import path

from .views import (
    ArticleLCView,
    ArticleRUDView,
    CommentLCView,
    CommentRUDView,
)


urlpatterns = [
    path('article-lc/', ArticleLCView.as_view(), name='article-lc'),
    path('article-rud/<slug:slug>/', ArticleRUDView.as_view(), name='article-rud'),
    path('comment-lc/', CommentLCView.as_view(), name='comment-lc'),
    path('comment-rud/<int:pk>/', CommentRUDView.as_view(), name='comment-rud'),
]
