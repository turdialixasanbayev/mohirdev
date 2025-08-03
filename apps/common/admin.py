from django.contrib import admin


admin.site.site_header = "mohirdev Admin Paneli"
admin.site.site_title = "mohirdev Admin Paneli"
admin.site.index_title = "mohirdev Admin Paneliga Xush Kelibsiz!"

from .models import SubEmail, Notification, Statistics, Partners, Testimonials, Banner, Certificate


admin.site.register(SubEmail)
admin.site.register(Notification)
admin.site.register(Statistics)
admin.site.register(Partners)
admin.site.register(Testimonials)
admin.site.register(Banner)
admin.site.register(Certificate)
