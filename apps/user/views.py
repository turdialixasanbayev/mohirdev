from rest_framework import generics

from .models import (
    CustomUser,
)
from .serializers import (
    CustomUserLCSerializer,
    CustomUserRUDSerializer,
)


class CustomUserLCView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserLCSerializer


class CustomUserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserRUDSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
