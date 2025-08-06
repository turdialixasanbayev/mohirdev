from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    CustomUser Admin Interface
    """
    model = CustomUser
    ordering = ('phone_number',)
    list_display = (
        'id',
        'phone_number',
        'get_role',
        'username',
        'email',
        'get_full_name',
        'first_name',
        'last_name',
        'image',
        'get_age',
        'get_gender',
        'get_full_location',
        'country',
        'city',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
    )
    search_fields = (
        'phone_number',
        'username',
        'email',
        'first_name',
        'last_name',
        'country',
        'city',
        'age',
    )
    readonly_fields = (
        'id',
        'last_login',
        'date_joined',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'role',
        'gender',
    )
    fieldsets = (
        ('Login', {
            'fields': ('phone_number', 'password',),
            'classes': ('wide',),
        }),
        ('Personal Info', {
            'fields': ('username', 'first_name', 'last_name', 'email', 'image', 'bio',),
            'classes': ('wide',),
        }),
        ('Location Info', {
            'fields': ('country', 'city',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
            'classes': ('wide',),
        }),
        ("Role and Gender and Age", {
            'fields': ('role', 'gender', 'age',),
            'classes': ('wide',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',),
        }),
    )
    add_fieldsets = (
        ('Create User (user, admin, teacher)', {
            'fields': ('phone_number', 'password1', 'password2',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff',),
            'classes': ('wide',),
        }),
        ("Role", {
            'fields': ('role',),
            'classes': ('wide',),
        }),
    )
