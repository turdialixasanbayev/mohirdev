from django.contrib import admin

from .models import Comment, Article, LikeArticle


class ArticleAdmin(admin.ModelAdmin):
    """
    Article model admin interface.
    """
    ordering = ('-name',)
    model = Article
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'id',
        'name',
        'image',
        'video',
        'link',
        'category',
        'author',
        'views_count',
        'duration',
        'likes_count',
        'dislikes_count',
        'total_reactions',
        'reaction_status',
        'comments_count',
        'rating',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'author',
        'is_active',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'likes_count',
        'dislikes_count',
        'total_reactions',
        'reaction_status',
        'comments_count',
        'rating',
    )


admin.site.register(Article, ArticleAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment model admin interface.
    """
    ordering = ('-created_at',)
    model = Comment
    list_display = (
        'id',
        'user',
        'article',
        'rate',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('article__name',)
    list_filter = (
        'is_active',
        'user',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(LikeArticle)
class LikeArticleAdmin(admin.ModelAdmin):
    """
    LikeArticle model admin interface.
    """
    ordering = ('-created_at',)
    model = LikeArticle
    list_display = (
        'id',
        'user',
        'article',
        'status',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('article__name',)
    list_filter = (
        'is_active',
        'user',
        'like_or_dislike',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'status',
    )
