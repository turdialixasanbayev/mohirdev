from rest_framework import generics

from .models import (
    Article,
    Comment,
    LikeArticle,
)
from apps.common import permissions
from .serializers import (
    ArticleLCSerializer,
    ArticleRUDSerializer,
    CommentLCSerializer,
    CommentRUDSerializer,
    LikeArticleLCSerializer,
    LikeArticleRUDSerializer,
)
from .filters import (
    ArticleFilter,
    CommentFilter,
    LikeArticleFilter,
)


class ArticleLCView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleLCSerializer
    permission_classes = [permissions.IsAdmin]
    filterset_class = ArticleFilter

    def get_queryset(self):
        return self.queryset.select_related(
            'author',
            'category',
        ).prefetch_related(
            'tags',
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleRUDSerializer
    permission_classes = [permissions.IsAdmin]
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.select_related(
            'author',
            'category',
        ).prefetch_related(
            'tags',
        )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentLCView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentLCSerializer
    filterset_class = CommentFilter

    def get_queryset(self):
        return self.queryset.select_related('user', 'article')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('user', 'article')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class LikeArticleLCView(generics.ListCreateAPIView):
    queryset = LikeArticle.objects.filter(is_active=True)
    serializer_class = LikeArticleLCSerializer
    filterset_class = LikeArticleFilter

    def get_queryset(self):
        return self.queryset.select_related('article', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeArticleRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikeArticle.objects.filter(is_active=True)
    serializer_class = LikeArticleRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('article', 'user')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
