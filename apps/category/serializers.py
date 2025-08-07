from rest_framework import serializers

from .models import (
    Tag,
    Category,
)


class TagLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]


class TagRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]


class CategoryLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]


class CategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]
