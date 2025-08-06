from django.db import models

from django.db.models import Avg
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

import uuid

from decimal import Decimal

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel
from apps.category.models import CategoryRole, Category, Tag


class Course(BaseModel):
    """Course model"""
    PRICE_TYPE = (
        ('free', 'Free'),
        ('uzs', "🇺🇿 So'm"),
        ('rub', '₽ Rubl'),
        ('eur', '€ Yevro'),
        ('usd', '$ AQSh dollari'),
    )
    class Level(models.TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'
    LANGUAGE = (
        ('uz', "O'zbek"),
        ('ru', 'Русский'),
        ('en', 'English'),
    )
    class Duration(models.TextChoices):
        ONE_MONTH = '1m', '1 oylik'
        THREE_MONTHS = '3m', '3 oylik'
        SIX_MONTHS = '6m', '6 oylik'
        ONE_YEAR = '1y', '1 yillik'
    title = models.CharField(max_length=300, unique=True, db_index=True)
    sub_title = models.CharField(max_length=300, blank=True, null=True, db_index=True, unique=True)
    slug = models.SlugField(max_length=400, unique=True, db_index=True, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category', limit_choices_to={'role': CategoryRole.COURSE})
    tags = models.ManyToManyField(Tag, related_name='course_tags', blank=True)
    teacher = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='course_teacher', limit_choices_to={'role': 'teacher'})
    is_free = models.BooleanField(default=True)
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE, default='free')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    percentage = models.IntegerField(default=0)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.BEGINNER)
    language = models.CharField(max_length=10, choices=LANGUAGE, default='uz')
    duration = models.CharField(max_length=10, choices=Duration.choices, default=Duration.ONE_MONTH)
    students_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.is_free:
            if self.price and self.price > 0:
                raise ValidationError("Bepul kurslar uchun narx belgilab bo'lmaydi.")
            if self.price_type != 'free':
                raise ValidationError("Bepul kurslar uchun price_type 'free' bo'lishi kerak.")
        else:
            if not self.price or self.price <= 0:
                raise ValidationError("Pullik kurslar uchun narxni kiriting.")
            if self.price_type == 'free':
                raise ValidationError("Pullik kurslar uchun to'g'ri valyuta tanlang.")

    @property
    def rating(self):
        average = self.review_course.aggregate(avg=Avg('rate'))['avg']
        return round(average, 1) if average else 0

    @property
    def reviews_count(self):
        return self.review_course.count()

    @property
    def lessons_count(self):
        return self.lesson_course.count()

    @property
    def full_price(self):
        if self.is_free and self.price_type == 'free':
            return "Bepul"
        return f"{self.price} {self.get_price_type_display()}"

    @property
    def discount(self):
        if self.price and self.percentage:
            return (self.price * Decimal(self.percentage)) / Decimal(100)
        return None

    @property
    def discount_price(self):
        if self.discount is not None:
            return self.price - self.discount
        return self.price

    @property
    def get_percentage(self):
        if self.percentage:
            return f"{self.percentage} %"
        return "Chegirma yo'q"

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            date_slug = timezone.now().strftime("%d-%m-%Y-%H-%M-%S")
            uuid_slug = str(uuid.uuid4().hex[:8])
            self.slug = f"{base_slug}-{date_slug}-{uuid_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} {self.title}"


class Review(BaseModel):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='review_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course')
    comment = RichTextField(null=True, blank=True)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)

    def __str__(self):
        return f"{self.pk} {self.course.title}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson_course')
    name = models.CharField(max_length=300, db_index=True, unique=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True, null=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='lesson_images', null=True, blank=True)
    file = models.FileField(upload_to='lesson_files', null=True, blank=True)
    video = models.FileField(upload_to='lesson_videos', null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, blank=True, related_name='lesson_tags')
    url = models.URLField(max_length=300, null=True, blank=True)
    views_count = models.IntegerField(default=0)
    is_preview = models.BooleanField(default=True)

    @property
    def likes_count(self):
        return self.like_lesson.filter(like_or_dislike=1).count()

    @property
    def dislikes_count(self):
        return self.like_lesson.filter(like_or_dislike=0).count()

    @property
    def total_reactions(self):
        return self.like_lesson.count()

    @property
    def reaction_status(self):
        reactions = self.like_lesson.values_list('like_or_dislike', flat=True)

        if 1 in reactions:
            return "Layk"
        elif 0 in reactions:
            return "Dislike"
        else:
            return "None"

    class Meta:
        verbose_name = 'Video dars'
        verbose_name_plural = 'Video darslar'

    def __str__(self):
        return f"{self.pk} {self.name} {self.course.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            date_slug = timezone.now().strftime("%d-%m-%Y")
            uuid_slug = str(uuid.uuid4().hex[:6])
            self.slug = f"{base_slug}-{date_slug}-{uuid_slug}"
        super().save(*args, **kwargs)


class Like(BaseModel):
    LIKE_OR_DISLIKE = (
        (0, 'Dislike'),
        (1, 'Like'),
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='like_lesson')
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='like_user')
    like_or_dislike = models.IntegerField(choices=LIKE_OR_DISLIKE, default=0)

    class Meta:
        verbose_name = 'Yoqtirish'
        verbose_name_plural = 'Yoqtirishlar'
        constraints = [
            models.UniqueConstraint(fields=['lesson', 'user'], name='unique_lesson_user')
        ]

    def __str__(self):
        return f"{self.pk} {self.lesson.name}"


class FAQ(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faq_course')
    question = models.CharField(max_length=300, db_index=True, unique=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return f"{self.pk} {self.question}"
