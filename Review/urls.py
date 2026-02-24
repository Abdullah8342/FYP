from django.urls import path
from .views import ReviewCreate,ReviewUpdateDestroy


urlpatterns = [
    path('review/',ReviewCreate.as_view(),name="review-create"),
    path('review/<int:pk>/',ReviewUpdateDestroy.as_view(),name="review-update-destroy"),
]
