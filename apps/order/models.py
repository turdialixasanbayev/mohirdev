from django.db import models

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from ..common.models import BaseModel


class Order(BaseModel):
    STATUS = (
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.CASCADE, related_name='order_user')
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    phone_number = PhoneNumberField(max_length=15, region='UZ', db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    address = models.CharField(max_length=255, db_index=True)
    notes = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.pk} {self.status}"


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_item_order')
    course = models.ForeignKey(
        'course.Course', on_delete=models.CASCADE, related_name='order_item_course')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.pk} {self.course.title}"
