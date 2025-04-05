from django.urls import path
from .views import CheckUserAPIView, CompleteRegistrationAPIView, LoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/<uuid:org_uuid>/register/check/", CheckUserAPIView.as_view(), name="check_user"),
    path("auth/<uuid:org_uuid>/register/complete/", CompleteRegistrationAPIView.as_view(), name="complete_registration"),
    path("auth/<uuid:org_uuid>/login/", LoginAPIView.as_view(), name="login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
