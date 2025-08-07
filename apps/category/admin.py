from django.contrib import admin

from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category model admin interface.
    """
    model = Category
    ordering = ('-created_at',)
    list_display = (
        'id',
        'role',
        'parent',
        'name',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('name',)
    list_filter = ('is_active', 'role', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Tag model admin interface.
    """
    model = Tag
    ordering = ('-id',)
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
