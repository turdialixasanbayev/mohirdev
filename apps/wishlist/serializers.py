from rest_framework import serializers

from .models import (
    WishList,
    WishListItem,
)
from apps.user.serializers import CustomUserLCSerializer


class WishListLCSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'


class WishListRUDSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'


class WishListItemLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = '__all__'


class WishListItemRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = '__all__'
