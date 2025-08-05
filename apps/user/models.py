from django.db import models

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

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
    phone_number = PhoneNumberField(max_length=15, unique=True, db_index=True, region="UZ", help_text='Telefon raqamingizni kiriting: ')
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

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return None

    @property
    def get_role(self):
        if self.role == 'user':
            return "Foydalanuvchi"
        elif self.role == 'teacher':
            return "O'qituvchi"
        elif self.role == 'admin':
            return "Admin"
        else:
            return None

    @property
    def get_age(self):
        if self.age:
            return f"{self.age} yosh"
        return None

    @property
    def get_gender(self):
        if self.gender == 'erkak':
            return "Erkak"
        elif self.gender == 'ayol':
            return "Ayol"
        else:
            return None

    @property
    def get_full_location(self):
        if self.country and self.city:
            return f"{self.country} - {self.city}"
        else:
            return None
