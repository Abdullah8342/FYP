from django.urls import path
from .views import HelperServiceView, HelperServiceDetailsView

urlpatterns = [
    path("helperservice/", HelperServiceView.as_view(), name="helper-service"),
    path(
        "helperservice/<int:pk>/",
        HelperServiceDetailsView.as_view(),
        name="helper-service-details",
    ),
]
