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
    telegram_username = models.CharField(max_length=100, blank=True, null=True, db_index=True, unique=True)

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
