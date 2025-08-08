from rest_framework import serializers

from .models import (
    CustomUser,
)


class CustomUserLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
