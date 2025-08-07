from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    ContactUs model admin interface.
    """
    ordering = ('-created_at',)
    model = ContactUs
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'link',
        'subject',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
        'phone_number',
        'link',
        'subject',
    )
