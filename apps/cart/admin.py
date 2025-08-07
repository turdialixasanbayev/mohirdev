from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Cart model admin interface.
    """
    model = Cart
    ordering = ('-created_at',)
    list_display = (
        'id',
        'user',
        'cart_sub_total_price',
        'cart_total_price',
        'items_count',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'cart_sub_total_price',
        'cart_total_price',
        'items_count',
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('user__phone_number',)
    list_filter = ('is_active', 'user', 'created_at', 'updated_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    CartItem model admin interface.
    """
    model = CartItem
    ordering = ('-id',)
    list_display = (
        'id',
        'cart',
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
    search_fields = ('cart__user__phone_number', 'course__title',)
    list_filter = ('is_active',)
