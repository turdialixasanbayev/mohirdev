from django.contrib import admin

from .models import SubEmail, Notification, Statistics, Partners, Testimonials, Banner, Certificate


admin.site.site_header = "mohirdev Admin Paneli"
admin.site.site_title = "mohirdev Admin Paneli"
admin.site.index_title = "mohirdev Admin Paneliga Xush Kelibsiz!"


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    """
    SubEmail model admin interface
    """
    model = SubEmail
    ordering = ('-created_at',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'telegram_username',
        'is_active',
        "created_at",
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
        'phone_number',
        'telegram_username',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Notification model admin interface
    """
    model = Notification
    ordering = ('-id',)
    search_fields = ('name',)
    list_display = (
        'id',
        'user',
        'name',
        'is_read',
        'is_active',
        "created_at",
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_read',
        'user',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    """
    Statistics model admin interface
    """
    model = Statistics
    ordering = ('-created_at',)
    search_fields = ('key',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'key',
        'is_active',
        "created_at",
        'updated_at',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    """
    Partners model admin interface
    """
    model = Partners
    ordering = ('-created_at',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'name',
        'image',
        'is_active',
        "created_at",
        'updated_at',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    """
    Testimonials model admin interface
    """
    model = Testimonials
    ordering = ('-id',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'name',
        'image',
        'video',
        'link',
        'is_active',
        "created_at",
        'updated_at',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    """
    Banner model admin interface
    """
    model = Banner
    ordering = ('-id',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display = (
        'id',
        'name',
        'image',
        'video',
        'link',
        'is_active',
        "created_at",
        'updated_at',
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """
    Certificate model admin interface
    """
    model = Certificate
    ordering = ('-created_at',)
    list_display = (
        'id',
        'user',
        'course',
        'file',
        'is_active',
        "created_at",
        'updated_at',
    )
    search_fields = (
        'user__phone_number',
        'course__title',
    )
    list_filter = (
        'is_active',
        'user',
        'created_at',
        'updated_at'
    )
    readonly_fields = (
        'id',
        "created_at",
        'updated_at',
    )
