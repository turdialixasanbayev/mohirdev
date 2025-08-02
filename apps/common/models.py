from django.db import models

from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, db_index=True, unique=True)
    telegram_username = models.URLField(max_length=200, blank=True, null=True, db_index=True, unique=True)

    def __str__(self):
        return f"ID: {self.pk} Name: {self.name} Email: {self.email} Phone: {self.phone_number} Telegram: {self.telegram_username}"

    class Meta:
        verbose_name = 'SubEmail'
        verbose_name_plural = 'SubEmails'


class Notification(BaseModel):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='notification_user')
    name = models.CharField(max_length=100, db_index=True)
    message = RichTextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"ID: {self.pk} Name: {self.name}"

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
        return f"ID: {self.pk} Key: {self.key} Value: {self.value}"


class Partners(BaseModel):
    name = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to='partners', blank=True, null=True)

    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'

    def __str__(self):
        return f"ID: {self.pk} Name: {self.name}"


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
        return f"ID: {self.pk} Name: {self.name}"


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
        return self.name
