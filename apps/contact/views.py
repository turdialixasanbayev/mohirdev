from rest_framework import viewsets

from .models import (
    ContactUs,
)
from .serializers import (
    ContactUsSerializer,
)


class ContactUsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contact us instances.
    """
    queryset = ContactUs.objects.filter(is_active=True)
    serializer_class = ContactUsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
