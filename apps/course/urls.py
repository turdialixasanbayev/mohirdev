from django.urls import path, include

from .views import (
    CourseCreateView,
    CourseDeleteView,
    CourseListView,
    CourseUpdateView,
    CourseDetailView,
    ReviewViewSet,
    FAQViewSet,
    LessonLCView,
    LessonRUDView,
    LikeLCView,
    LikeRUDView,
)

from rest_framework import (
    routers,
)


router = routers.DefaultRouter()

router.register(r'reviews', ReviewViewSet)
router.register(r'faqs', FAQViewSet)


urlpatterns = [
    path('viewsets/', include(router.urls)),
    path(
        'course-create/',
        CourseCreateView.as_view(),
        name='course-create',
    ),
    path(
        'course-delete/<slug:slug>/',
        CourseDeleteView.as_view(),
        name='course-delete',
    ),
    path(
        'course-list/',
        CourseListView.as_view(),
        name='course-list',
    ),
    path(
        'course-update/<slug:slug>/',
        CourseUpdateView.as_view(),
        name='course-update',
    ),
    path(
        'course-detail/<slug:slug>/',
        CourseDetailView.as_view(),
        name='course-detail',
    ),
    path(
        'lessons/',
        LessonLCView.as_view(),
        name='lesson-lc',
    ),
    path(
        'lessons/<slug:slug>/',
        LessonRUDView.as_view(),
        name='lesson-rud',
    ),
    path(
        'likes/',
        LikeLCView.as_view(),
        name='like-lc',
    ),
    path(
        'likes/<int:pk>/',
        LikeRUDView.as_view(),
        name='like-rud',
    ),
]
