from rest_framework import (
    viewsets,
)

from .models import (
    Order,
    OrderItem,
)

from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.select_related(
            'user'
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.filter(is_active=True)
    serializer_class = OrderItemSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return self.queryset.select_related(
            'course',
            'order'
        )
