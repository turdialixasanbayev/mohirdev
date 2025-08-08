from rest_framework import generics

from .models import (
    Cart,
    CartItem,
)
from .serializers import (
    CartItemLCSerializer,
    CartItemRUDSerializer,
    CartLCSerializer,
    CartRUDSerializer,
)


class CartLCView(generics.ListCreateAPIView):
    queryset = Cart.objects.filter(is_active=True)
    serializer_class = CartLCSerializer

    def get_queryset(self):
        return self.queryset.select_related('user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.filter(is_active=True)
    serializer_class = CartRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('user')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CartItemLCView(generics.ListCreateAPIView):
    queryset = CartItem.objects.filter(is_active=True)
    serializer_class = CartItemLCSerializer

    def get_queryset(self):
        return self.queryset.select_related('cart', 'course')


class CartItemRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.filter(is_active=True)
    serializer_class = CartItemRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related('cart', 'course')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
