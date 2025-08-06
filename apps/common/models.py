from django.db import models

from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'
        abstract = True


class SubEmail(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    phone_number = PhoneNumberField(region='UZ', max_length=15, unique=True, db_index=True, help_text="Telefon raqamingiz, masalan: +998901234567")
    telegram_username = models.URLField(max_length=200, blank=True, null=True, db_index=True, unique=True)

    def __str__(self):
        return f"{self.pk} {self.email}"

    class Meta:
        verbose_name = 'SubEmail'
        verbose_name_plural = 'SubEmails'


class Notification(BaseModel):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='notification_user')
    name = models.CharField(max_length=100, db_index=True)
    message = RichTextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} {self.name}"

    class Meta:
        verbose_name = 'Xabarnoma'
        verbose_name_plural = 'Xabarnomalar'


class Statistics(BaseModel):
    key = models.CharField(max_length=250, db_index=True, unique=True)
    value = models.IntegerField()

    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural = 'Statistikalar'

    def __str__(self):
        return f"{self.pk} {self.key} {self.value}"


class Partners(BaseModel):
    name = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='partners', blank=True, null=True)

    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'

    def __str__(self):
        return f"{self.pk} {self.name}"


class Testimonials(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='testimonials_image', blank=True, null=True)
    video = models.FileField(upload_to='testimonials_video', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    message = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Fikr'
        verbose_name_plural = 'Fikrlar'

    def __str__(self):
        return f"{self.pk} {self.name}"


class Banner(BaseModel):
    name = models.CharField(max_length=256, db_index=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="banner_images/")
    video = models.FileField(upload_to="banner_videos/", blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

    def __str__(self):
        return f"{self.pk} {self.name}"


class Certificate(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificate_user')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='certificate_course')
    file = models.FileField(upload_to='certificates/', blank=True, null=True)

    class Meta:
        verbose_name = 'Sertifikat'
        verbose_name_plural = 'Sertifikatlar'
        constraints = [
        models.UniqueConstraint(fields=['user', 'course'], name='unique_user_course')
    ]

    def __str__(self):
        return f"{self.pk} {self.user.phone_number} {self.course.title}"
