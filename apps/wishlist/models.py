from django.db import models

from ..common.models import BaseModel


class WishList(BaseModel):
    user = models.OneToOneField('user.CustomUser', on_delete=models.CASCADE, related_name='wishlist_user')

    @property
    def items_count(self):
        return self.wishlistitem_wishlist.count()

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"

    def __str__(self):
        return f"{self.pk} - {self.user.phone_number}"


class WishListItem(BaseModel):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='wishlistitem_wishlist')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='wishlistitem_course')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['wishlist', 'course'], name='unique_wishlist_course')
        ]
        verbose_name = "WishList Item"
        verbose_name_plural = "WishList Items"

    def __str__(self):
        return f"{self.pk} - {self.course.title}"
