import django_filters as filter

from .models import (
    Tag,
    Category,
    CategoryRole,
)


class TagFilter(filter.FilterSet):
    is_active = filter.BooleanFilter()
    name = filter.CharFilter(lookup_expr='icontains')
    slug = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tag
        fields = [
            'name',
            'slug',
            'is_active',
        ]


class CategoryFilter(filter.FilterSet):
    is_active = filter.BooleanFilter()
    name = filter.CharFilter(lookup_expr='icontains')
    slug = filter.CharFilter(lookup_expr='icontains')
    role = filter.ChoiceFilter(choices=CategoryRole.choices)
    parent = filter.ModelChoiceFilter(queryset=Category.objects.filter(parent__isnull=True))

    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'role',
            'parent',
            'is_active',
        ]
