from rest_framework import generics

from .serializers import (
    TagLCSerializer,
    TagRUDSerializer,
    CategoryLCSerializer,
    CategoryRUDSerializer,
)
from .models import (
    Tag,
    Category,
)
from .filters import (
    TagFilter,
    CategoryFilter,
)
from apps.common import permissions


class TagLCView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagLCSerializer
    filterset_class = TagFilter
    permission_classes = [permissions.IsAdmin]


class TagRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagRUDSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdmin]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class CategoryLCView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryLCSerializer
    filterset_class = CategoryFilter
    permission_classes = [permissions.IsAdmin]


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryRUDSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdmin]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
