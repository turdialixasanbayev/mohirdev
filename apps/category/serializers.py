from rest_framework import serializers

from .models import (
    Tag,
    Category,
)


class TagLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategoryLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
