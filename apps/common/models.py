from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Asosiy Model'
        verbose_name_plural = 'Asosiy Model'


class SubEmail(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, db_index=True)
    telegram_username = models.CharField(max_length=100, blank=True, null=True, db_index=True, unique=True)

    def __str__(self):
        return f"ID: {self.pk} Name: {self.name} Email: {self.email} Phone: {self.phone_number} Telegram: {self.telegram_username}"
    
    class Meta:
        verbose_name = 'SubEmail'
        verbose_name_plural = 'SubEmails'
        ordering = ['name', 'email', 'phone_number', 'telegram_username']
