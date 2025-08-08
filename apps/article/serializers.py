from rest_framework import serializers

from .models import (
    Article,
)
from apps.user.serializers import (
    CustomUserLCSerializer,
)


class ArticleLCSerializer(serializers.ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class ArticleRUDSerializer(serializers.ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
