from django.contrib import admin

from .models import Course, Review, Lesson, Like, FAQ


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Course model admin interface.
    """
    model = Course
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',),}
    search_fields = ('title',)
    list_display = (
        'id',
        'title',
        'image',
        'category',
        'teacher',
        'is_free',
        'price_type',
        'price',
        'level',
        'language',
        'duration',
        'students_count',
        'is_published',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_free',
        'is_active',
        'teacher',
        'is_published',
        'price_type',
        'level',
        'language',
        'duration',
    )
    readonly_fields = (
        'id',
        'rating',
        'reviews_count',
        'lessons_count',
        'full_price',
        'discount',
        'discount_price',
        'get_percentage',
        'created_at',
        'updated_at',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review admin.
    """
    ordering = ('-id',)
    model = Review
    list_display = (
        'id',
        'user',
        'course',
        'rate',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__phone_number',
        'course__title',
    )
    list_filter = (
        'user',
        'is_active',
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    FAQ admin.
    """
    ordering = ('-id',)
    list_filter = ('is_active',)
    model = FAQ
    list_display = (
        'id',
        'course',
        'question',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'course__title',
        'question',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Lesson admin.
    """
    model = Lesson
    ordering = ('-created_at',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',),}
    list_display = (
        'id',
        'course',
        'name',
        'image',
        'file',
        'video',
        'duration',
        'url',
        'views_count',
        'is_preview',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'likes_count',
        'dislikes_count',
        'total_reactions',
        'reaction_status',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_preview',
        'created_at',
        'updated_at',
    )


class LikeAdmin(admin.ModelAdmin):
    """
    Like admin.
    """
    model = Like
    ordering = ('-created_at',)
    list_display = (
        'id',
        'lesson',
        'user',
        'like_or_dislike',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'user',
        'like_or_dislike',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__phone_number',
        'lesson__name',
    )


admin.site.register(Like, LikeAdmin)
