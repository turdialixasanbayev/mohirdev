from django.urls import path

from .views import (
    CustomUserLCView,
    CustomUserRUDView,
)


urlpatterns = [
    path('custom-user-lc/', CustomUserLCView.as_view(), name='custom-user-lc'),
    path('custom-user-rud/<int:pk>/', CustomUserRUDView.as_view(), name='custom-user-rud'),
]
