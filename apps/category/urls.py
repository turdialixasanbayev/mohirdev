from django.urls import path

from .views import (
    TagLCView,
    TagRUDView,
    CategoryLCView,
    CategoryRUDView,
)


urlpatterns = [
    path('tag-lc/', TagLCView.as_view(), name='tag-lc'),
    path('tag-rud/<slug:slug>/', TagRUDView.as_view(), name='tag-rud'),
    path('category-lc/', CategoryLCView.as_view(), name='category-lc'),
    path('category-rud/<slug:slug>/', CategoryRUDView.as_view(), name='category-rud'),
]
