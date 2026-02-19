from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import SignupView,LogoutView
urlpatterns = [
    path("signup/", SignupView.as_view(),name='signup'),
    path("logout/", LogoutView.as_view(),name='logout'),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
]
