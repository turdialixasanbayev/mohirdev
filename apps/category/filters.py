import django_filters as filter

from .models import (
    Tag,
    Category,
)


class TagFilter(filter.FilterSet):
    id = filter.NumberFilter()
    is_active = filter.BooleanFilter()
    created_at = filter.DateFromToRangeFilter()
    updated_at = filter.DateFromToRangeFilter()
    name = filter.CharFilter(lookup_expr='icontains')
    slug = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]


class CategoryFilter(filter.FilterSet):
    id = filter.NumberFilter()
    is_active = filter.BooleanFilter()
    created_at = filter.DateFromToRangeFilter()
    updated_at = filter.DateFromToRangeFilter()
    name = filter.CharFilter(lookup_expr='icontains')
    slug = filter.CharFilter(lookup_expr='icontains')
    role = filter.ChoiceFilter(choices=Category._meta.get_field('role').choices)
    parent = filter.ModelChoiceFilter(queryset=Category.objects.filter(parent__isnull=True))

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'role',
            'parent',
            'is_active',
            'created_at',
            'updated_at',
        ]
