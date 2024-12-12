# api/urls.py

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserCreateView, EventCreateView
)

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('events/', EventCreateView.as_view(), name='event-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
