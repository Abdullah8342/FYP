from django.urls import path
from .views import BookingView,BookingDetailsView

urlpatterns = [
    path('bookings/',BookingView.as_view(),name='bookings'),
    path('bookings/<int:pk>/',BookingDetailsView.as_view(),name='bookings-details'),
]
