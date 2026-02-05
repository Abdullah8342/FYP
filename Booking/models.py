from django.db import models
from django.contrib.auth.models import User
from Helper.models import HelperService
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
        ("In Progress", "In Progress"),
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    helper_service = models.ForeignKey(
        HelperService, on_delete=models.CASCADE, related_name="helper_service"
    )
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="Pending")
    scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.helper_service} - {self.status}"

    def clean(self):

        if self.user == self.helper_service.user:
            raise ValidationError("You Cannot Book Your Own Service")

        if not self.helper_service.is_available:
            raise ValidationError("Unavailable Service")


        min_time = timezone.now() + timezone.timedelta(minutes=15)
        if self.scheduled_at < min_time:
            raise ValidationError("Booking must be at least 15 minutes in the future.")

        conflict = (
            Booking.objects.filter(
                helper_service=self.helper_service,
                scheduled_at=self.scheduled_at,
                status__in=["Pending", "Accepted"],
            )
            .exclude()
            .exists()
        )

        if conflict:
            raise ValidationError("Helper already booked at this time")
        return super().clean()
