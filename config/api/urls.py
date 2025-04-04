from django.urls import path
from .views import CheckUserAPIView, CompleteRegistrationAPIView

urlpatterns = [
    path("auth/<uuid:org_uuid>/register/check/", CheckUserAPIView.as_view(), name="check_user"),
    path("auth/<uuid:org_uuid>/register/complete/", CompleteRegistrationAPIView.as_view(), name="complete_registration"),
]
