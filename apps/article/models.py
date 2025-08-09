from django.db import models

from django.db.models import Avg
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from ckeditor.fields import RichTextField

import uuid

from apps.common.models import BaseModel
from apps.category.models import Category, Tag, CategoryRole


class Article(BaseModel):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)
    video = models.FileField(upload_to='article_videos', null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article_category', limit_choices_to={'role': CategoryRole.ARTICLE})
    tags = models.ManyToManyField(Tag, related_name='article_tags', blank=True)
    author = models.ForeignKey(
        to='user.CustomUser',
        on_delete=models.CASCADE,
        related_name='article_author',
        limit_choices_to={'is_author': True}
    )
    views_count = models.IntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)

    @property
    def likes_count(self):
        return self.likearticle_article.filter(like_or_dislike=1).count()

    @property
    def dislikes_count(self):
        return self.likearticle_article.filter(like_or_dislike=0).count()

    @property
    def total_reactions(self):
        return self.likearticle_article.count()

    @property
    def reaction_status(self):
        reactions = self.likearticle_article.values_list('like_or_dislike', flat=True)

        if 1 in reactions:
            return "Layk"
        elif 0 in reactions:
            return "Dislike"
        else:
            return "None"

    @property
    def comments_count(self):
        return self.comment_article.count()

    @property
    def rating(self):
        average = self.comment_article.aggregate(avg=Avg('rate'))['avg']
        return round(average, 1) if average else 0

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return f"{self.pk} {self.name}"

    def get_absolute_url(self, *args, **kwargs):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = self.name.lower().replace(' ', '-')
            uuid_slug = str(uuid.uuid4())
            self.slug = f"{base_slug}-{uuid_slug}"
        super().save(*args, **kwargs)


class Comment(BaseModel):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='comment_user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_article')
    comment = RichTextField(null=True, blank=True)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)

    def __str__(self):
        return f"{self.pk} {self.article.name}"

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class LikeArticle(BaseModel):
    LIKE_OR_DISLIKE = (
        (0, 'Dislike'),
        (1, 'Like'),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likearticle_article')
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='likearticle_user')
    like_or_dislike = models.IntegerField(choices=LIKE_OR_DISLIKE, default=0)

    @property
    def status(self):
        return self.LIKE_OR_DISLIKE[self.like_or_dislike][1]

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        constraints = [
            models.UniqueConstraint(fields=['article', 'user'], name='unique_article_user')
        ]

    def __str__(self):
        return f"{self.pk} {self.article.name}"
