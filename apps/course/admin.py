from django.contrib import admin

from .models import Course, Review, Lesson, Like, FAQ


admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Lesson)
admin.site.register(Like)
admin.site.register(FAQ)
