from rest_framework import serializers

from .models import (
    Cart,
    CartItem,
)
from apps.user.serializers import CustomUserLCSerializer


class CartLCSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CartRUDSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
