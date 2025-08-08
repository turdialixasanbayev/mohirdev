from django.urls import path

from .views import (
    ArticleLCView,
    ArticleRUDView,
    CommentLCView,
    CommentRUDView,
    LikeArticleLCView,
    LikeArticleRUDView,
)


urlpatterns = [
    path('article-lc/', ArticleLCView.as_view(), name='article-lc'),
    path('article-rud/<slug:slug>/', ArticleRUDView.as_view(), name='article-rud'),
    path('comment-lc/', CommentLCView.as_view(), name='comment-lc'),
    path('comment-rud/<int:pk>/', CommentRUDView.as_view(), name='comment-rud'),
    path('like-article-lc/', LikeArticleLCView.as_view(), name='like-article-lc'),
    path('like-article-rud/<int:pk>/', LikeArticleRUDView.as_view(), name='like-article-rud'),
]
