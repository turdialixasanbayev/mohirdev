from django.db import models

from django.utils.text import slugify

from ckeditor.fields import RichTextField

import uuid
import datetime

from apps.common.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"

    def __str__(self):
        return f"{self.pk} - {self.name}"


class CategoryRole(models.TextChoices):
    ARTICLE = "article", "Article"
    COURSE = "course", "Course"


class Category(BaseModel):
    role = models.CharField(max_length=10, choices=CategoryRole.choices)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children", limit_choices_to={'parent__isnull': True})
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True, null=True)
    image = models.ImageField(upload_to="category_images", blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = str(uuid.uuid4())
            date_slug = datetime.datetime.now().strftime("%Y%m%d")
            self.slug = f"{base_slug}-{uuid_slug}-{date_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk} - Role: {self.role} - Name: {self.name}"

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
