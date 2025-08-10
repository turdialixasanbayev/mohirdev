from rest_framework import generics

from .models import (
    SubEmail,
    Notification,
    Statistics,
    Partners,
    Testimonials,
    Banner,
    Certificate,
)
from .serializers import (
    SubEmailSerializer,
    NotificationSerializer,
    StatisticsSerializer,
    PartnersSerializer,
    TestimonialsSerializer,
    BannerSerializer,
    CertificateSerializer,
    CertificateIsActiveStatusSerializer,
)


class SubEmailListCreateView(generics.ListCreateAPIView):
    queryset = SubEmail.objects.filter(is_active=True)
    serializer_class = SubEmailSerializer


class SubEmailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubEmail.objects.filter(is_active=True)
    serializer_class = SubEmailSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.filter(is_active=True)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.queryset.select_related(
            'user'
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NotificationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.filter(is_active=True)
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return self.queryset.select_related(
            'user'
        )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class StatisticsListCreateView(generics.ListCreateAPIView):
    queryset = Statistics.objects.filter(is_active=True)
    serializer_class = StatisticsSerializer
    pagination_class = None


class StatisticsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statistics.objects.filter(is_active=True)
    serializer_class = StatisticsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class PartnersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class PartnersListCreateView(generics.ListCreateAPIView):
    queryset = Partners.objects.filter(is_active=True)
    serializer_class = PartnersSerializer


class TestimonialsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonials.objects.filter(is_active=True)
    serializer_class = TestimonialsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class TestimonialsListCreateView(generics.ListCreateAPIView):
    queryset = Testimonials.objects.filter(is_active=True)
    serializer_class = TestimonialsSerializer


class BannerListCreateView(generics.ListCreateAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer


class BannerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class CertificateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificate.objects.filter(is_active=True)
    serializer_class = CertificateSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.select_related(
            'user',
            'course',
        ).order_by(
            '-created_at'
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CertificateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.filter(is_active=True)
    serializer_class = CertificateSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return self.queryset.select_related(
            'user',
            'course',
            ).order_by(
                '-created_at'
            )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CertificateIsActiveStatusAPIView(generics.UpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateIsActiveStatusSerializer
    lookup_field = 'pk'
