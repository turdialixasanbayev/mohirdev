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


class TagLCView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagLCSerializer


class TagRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagRUDSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class CategoryLCView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryLCSerializer


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryRUDSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
