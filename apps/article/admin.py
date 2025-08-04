from django.contrib import admin

from .models import Comment, Article, LikeArticle


admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(LikeArticle)
