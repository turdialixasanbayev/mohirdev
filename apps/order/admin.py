from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order model admin interface.
    """
    model = Order
    ordering = ('phone_number',)
    list_display = (
        'id',
        'user',
        'status',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'address',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'address',
    )
    list_filter = (
        'status',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Order item model admin interface.
    """
    model = OrderItem
    ordering = ('-id',)
    search_fields = ('course__title',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'order',
        'course',
        'price',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
