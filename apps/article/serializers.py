from rest_framework import serializers

from .models import (
    Article,
    Comment,
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


class CommentLCSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'


class CommentRUDSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
