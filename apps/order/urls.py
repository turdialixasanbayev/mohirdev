from django.urls import path, include

from rest_framework import (
    routers,
)

from .views import (
    OrderItemViewSet,
    OrderViewSet,
)


router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
