from rest_framework import (
    generics,
    viewsets,
)

from .serializers import (
    CourseCreateSerializer,
    CourseDeleteSerializer,
    CourseListSerializer,
    CourseUpdateSerializer,
    CourseDetailSerializer,
    ReviewSerializer,
    FAQSerializer,
    LessonSerializer,
    LikeSerializer,
)

from .models import (
    Course,
    Review,
    FAQ,
    Lesson,
    Like,
)


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

    def perform_create(self, serializer):
        serializer.save()  # You can add additional logic here if needed

    def get_queryset(self):
        return Course.objects.filter(is_active=True).select_related(
            'category',
            'teacher',
        ).prefetch_related(
            'tags',
        ).order_by('-created_at')


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDeleteSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related(
            'category',
            'teacher',
        ).prefetch_related(
            'tags',
        )


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.filter(is_active=True).select_related(
        'category',
        'teacher',
    ).prefetch_related(
        'tags',
    ).order_by(
        '-created_at',
    )
    serializer_class = CourseListSerializer

    def get_queryset(self):
        return self.queryset


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseUpdateSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Course.objects.filter(is_active=True).select_related(
            'category',
            'teacher',
        ).prefetch_related(
            'tags',
        )


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Course.objects.filter(is_active=True).select_related(
            'category',
            'teacher',
        ).prefetch_related(
            'tags',
        )


class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing review instances.
    """
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related(
            'course',
            'user',
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.filter(is_active=True).select_related('course')
    serializer_class = FAQSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class LessonLCView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).prefetch_related('tags').select_related('course')


class LessonRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Lesson.objects.filter(is_active=True).prefetch_related('tags').select_related('course')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class LikeLCView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related(
            'user',
            'lesson',
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Like.objects.filter(is_active=True).select_related(
            'user',
            'lesson',
        )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
