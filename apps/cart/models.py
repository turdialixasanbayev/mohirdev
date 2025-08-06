from django.db import models

from ..common.models import BaseModel


class Cart(BaseModel):
    """Cart model."""
    user = models.OneToOneField(
        to='user.CustomUser',
        on_delete=models.CASCADE,
        related_name='cart_user',
    )

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    @property
    def cart_sub_total_price(self):
        return sum(item.course.price for item in self.cart_item_cart.all())

    @property
    def cart_total_price(self):
        return sum(item.course.discount_price for item in self.cart_item_cart.all())

    @property
    def items_count(self):
        return self.cart_item_cart.count()

    def __str__(self):
        return f"{self.pk} - Cart ({self.user.phone_number})"


class CartItem(BaseModel):
    "Cart Item model."
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        related_name="cart_item_cart",
    )
    course = models.ForeignKey(
        to="course.Course",
        on_delete=models.CASCADE,
        related_name='cart_item_course',
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=['cart', 'course'], name='unique_cart_course')]
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return f"{self.pk} - {self.course.title}"
