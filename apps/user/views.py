from rest_framework import generics

from .models import (
    CustomUser,
)
from .serializers import (
    CustomUserLCSerializer,
    CustomUserRUDSerializer,
)
from .filters import (
    CustomUserFilter,
)
from apps.common import permissions


class CustomUserLCView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserLCSerializer
    filterset_class = CustomUserFilter
    permission_classes = [permissions.IsAdmin]


class CustomUserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserRUDSerializer
    permission_classes = [permissions.IsAdmin]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
