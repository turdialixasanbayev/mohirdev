from rest_framework import generics

from .models import (
    Article,
)
from apps.common import permissions
from .serializers import (
    ArticleLCSerializer,
    ArticleRUDSerializer,
)
from .filters import (
    ArticleFilter,
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
