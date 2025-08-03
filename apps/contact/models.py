from django.db import models

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


class ContactUs(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    phone_number = PhoneNumberField(max_length=15, db_index=True, region="UZ", help_text="Telefon raqamingizni kiriting: ")
    link = models.URLField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=100, db_index=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"ID: {self.pk} - Name: {self.name} - Email: {self.email}"

    class Meta:
        verbose_name = "Biz bilan aloqa!"
        verbose_name_plural = "Biz bilan aloqa!"
