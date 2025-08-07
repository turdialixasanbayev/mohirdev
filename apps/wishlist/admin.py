from django.contrib import admin

from .models import WishList, WishListItem


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    """
    WishList model admin interface.
    """
    model = WishList
    ordering = ('-id',)
    list_display = (
        'id',
        'user',
        'items_count',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'items_count',
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('user__phone_number',)
    list_filter = ('is_active', 'user',)


@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    """
    WishListItem model admin interface.
    """
    model = WishListItem
    ordering = ('-created_at',)
    list_display = (
        'id',
        'wishlist',
        'course',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('course__title',)
    list_filter = ('is_active',)
