import django_filters as filter

from .models import (
    CustomUser,
)


class CustomUserFilter(filter.FilterSet):
    is_staff = filter.BooleanFilter(field_name='is_staff')
    is_active = filter.BooleanFilter(field_name='is_active')
    is_superuser = filter.BooleanFilter(field_name='is_superuser')
    first_name = filter.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = filter.CharFilter(field_name="last_name", lookup_expr="icontains")
    email = filter.CharFilter(field_name="email", lookup_expr="icontains")
    role = filter.ChoiceFilter(field_name="role", choices=CustomUser.ROLE)
    phone_number = filter.CharFilter(field_name="phone_number", lookup_expr="icontains")
    gender = filter.ChoiceFilter(field_name="gender", choices=CustomUser.GENDER)
    country = filter.CharFilter(field_name="country", lookup_expr="icontains")
    city = filter.CharFilter(field_name="city", lookup_expr="icontains")
    age_min = filter.NumberFilter(field_name="age", lookup_expr="gte")
    age_max = filter.NumberFilter(field_name="age", lookup_expr="lte")

    class Meta:
        model = CustomUser
        fields = [
            'is_active',
            'is_staff',
            'is_superuser',
            'first_name',
            'last_name',
            'email',
            'role',
            'phone_number',
            'gender',
            'country',
            'city',
        ]
