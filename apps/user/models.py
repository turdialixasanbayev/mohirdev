from django.db import models

from ckeditor.fields import RichTextField

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ROLE = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('teacher', "O'qituvchi"),
    )
    GENDER = (
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
    )
    username = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, db_index=True)
    role = models.CharField(max_length=10, choices=ROLE, default='user')
    phone_number = models.CharField(max_length=20, unique=True, db_index=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    bio = RichTextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    city = models.CharField(max_length=100, null=True, blank=True, db_index=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return f"{self.phone_number} {self.role}"
