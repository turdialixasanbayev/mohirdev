from rest_framework import (
    serializers,
)

from .models import (
    Order,
    OrderItem,
)

from apps.user.serializers import (
    CustomUserLCSerializer,
)


class OrderSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
