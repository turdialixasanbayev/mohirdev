from django.urls import path

from .views import (
    WishListItemLCView,
    WishListItemRUDView,
    WishListLCView,
    WishListRUDView,
)


urlpatterns = [
    path('wishlist-lc/', WishListLCView.as_view(), name='wishlist-lc'),
    path('wishlist-rud/<int:pk>/', WishListRUDView.as_view(), name='wishlist-rud'),
    path('wishlist-item-lc/', WishListItemLCView.as_view(), name='wishlist-item-lc'),
    path('wishlist-item-rud/<int:pk>/', WishListItemRUDView.as_view(), name='wishlist-item-rud'),
]
