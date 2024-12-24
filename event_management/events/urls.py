from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ParticipantViewSet, NotificationViewSet, EventSearchView, RegisterView, LoginView


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('search/', EventSearchView.as_view(), name='search-events'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
