from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.conf import settings
from django.db import models
from Booking.models import Booking

# Create your models here.
User = settings.AUTH_USER_MODEL


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="review"
    )
    rating = models.PositiveIntegerField(default=3)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.booking}"

    def clean(self):
        print('Clean Is Running')
        if self.rating not in range(1,6):
            raise ValidationError("Rating Must Be From One To Five")
        if not self.booking.status == "Completed":
            raise ValidationError("Comment Only When Booking Is Completed")
        if not self.booking.user == self.user:
            raise ValidationError('Only Booked User Can Comment')
        if Review.objects.filter(user = self.user,booking = self.booking).exists():
            raise ValidationError('Only One Comment On One Booking')
        return super().clean()

    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)

    def get_average_rating(self):
        reviews = Review.objects.filter(
            booking=self.booking,helper_service__user=self.user
        )
        if not reviews.exists():
            return 0
        return reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"] or 0
