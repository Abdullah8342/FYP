from django.urls import path
from .views import ProfileView,ProfileDetailsView

urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/',ProfileDetailsView.as_view(),name='profile-view')
]
