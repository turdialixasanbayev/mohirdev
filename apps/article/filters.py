import django_filters as filter

from .models import (
    Article,
)


class ArticleFilter(filter.FilterSet):
    is_active = filter.BooleanFilter(field_name="is_active")
    name = filter.CharFilter(field_name="name", lookup_expr="icontains")
    description = filter.CharFilter(field_name="description", lookup_expr="icontains")
    category = filter.NumberFilter(field_name="category_id", lookup_expr="exact")
    author = filter.NumberFilter(field_name="author_id", lookup_expr="exact")
    tags = filter.NumberFilter(field_name="tags__id", lookup_expr="exact")
    views_min = filter.NumberFilter(field_name="views_count", lookup_expr="gte")
    views_max = filter.NumberFilter(field_name="views_count", lookup_expr="lte")
    duration_min = filter.DurationFilter(field_name="duration", lookup_expr="gte")
    duration_max = filter.DurationFilter(field_name="duration", lookup_expr="lte")

    class Meta:
        model = Article
        fields = [
            'is_active',
            'name',
            'description',
            'category',
            'author',
            'tags',
        ]
