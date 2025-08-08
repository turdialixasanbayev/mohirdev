from rest_framework import generics

from .models import (
    WishListItem,
    WishList,
)
from .serializers import (
    WishListItemLCSerializer,
    WishListItemRUDSerializer,
    WishListLCSerializer,
    WishListRUDSerializer,
)


class WishListLCView(generics.ListCreateAPIView):
    queryset = WishList.objects.filter(is_active=True)
    serializer_class = WishListLCSerializer

    def get_queryset(self):
        return self.queryset.select_related('user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishListRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.filter(is_active=True)
    serializer_class = WishListRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('user')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class WishListItemLCView(generics.ListCreateAPIView):
    queryset = WishListItem.objects.filter(is_active=True)
    serializer_class = WishListItemLCSerializer

    def get_queryset(self):
        return self.queryset.select_related('wishlist', 'course')


class WishListItemRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishListItem.objects.filter(is_active=True)
    serializer_class = WishListItemRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('wishlist', 'course')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
