from django.urls import path

from .views import (
    NextOfKinAPIView,
    NextOfKinDetailAPIView,
    ProfileDetailApiView,
    ProfileListAPIView,
)


urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all_profiles"),
    path("my-profile/", ProfileDetailApiView.as_view(), name="profile_detail"),
    path(
        "my-profile/next-of-kin/", NextOfKinAPIView.as_view(), name="next-of-kin-list"
    ),
    path(
        "my-profile/next-of-kin/<uuid:pk>/",
        NextOfKinDetailAPIView.as_view(),
        name="next-of-kin-detail",
    ),
]
