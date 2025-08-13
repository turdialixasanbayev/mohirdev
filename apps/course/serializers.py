from rest_framework import (
    serializers,
)

from .models import (
    Course,
    Review,
    FAQ,
    Lesson,
    Like,
)
from apps.category.serializers import (
    CategoryLCSerializer,
    TagLCSerializer,
)
from apps.user.serializers import (
    CustomUserLCSerializer,
)


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'slug': {'read_only': True},
            'id': {'read_only': True},
            'image': {'required': False},
            'is_free': {'required': False, 'default': False},
            'price_type': {'required': False, 'default': 'free'},
        }

        def validate(self, attrs):
            if attrs.get('is_free') and attrs.get('price_type') != 'free':
                raise serializers.ValidationError("If the course is free, the price type must be 'free'.")
            if attrs.get('price_type') == 'free' and not attrs.get('is_free'):
                raise serializers.ValidationError("For paid courses, select the correct currency.")
            return attrs


class CourseDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    category = CategoryLCSerializer(read_only=True)
    teacher = CustomUserLCSerializer(read_only=True)
    tags = TagLCSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = [
            'created_at',
            'id',
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryLCSerializer(read_only=True)
    teacher = CustomUserLCSerializer(read_only=True)
    tags = TagLCSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    class Meta:
        model = Like
        fields = '__all__'
