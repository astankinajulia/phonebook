from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import email_auth, obtain_token_by_email
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# router = routers.DefaultRouter()
# router.register(r'', ViewSet, basename='')

urlpatterns = [
    # path('v1/', include(router.urls)),
    path('v1/auth/email', email_auth, name='email_auth'),
    path('v1/auth/token', obtain_token_by_email, name='obtain_token_by_email'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
