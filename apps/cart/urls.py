from django.urls import path

from .views import (
    CartLCView,
    CartRUDView,
    CartItemRUDView,
    CartItemLCView,
)


urlpatterns = [
    path('cart-lc/', CartLCView.as_view(), name='cart-lc'),
    path('cart-rud/<int:pk>/', CartRUDView.as_view(), name='cart-rud'),
    path('cart-item-lc/', CartItemLCView.as_view(), name='cart-item-lc'),
    path('cart-item-rud/<int:pk>/', CartItemRUDView.as_view(), name='cart-item-rud'),
]
