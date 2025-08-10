from rest_framework import serializers

from .models import (
    SubEmail,
    Notification,
    Statistics,
    Partners,
    Testimonials,
    Banner,
    Certificate,
)
from apps.user.serializers import (
    CustomUserLCSerializer,
)


class SubEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubEmail
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'


class CertificateIsActiveStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['is_active']
