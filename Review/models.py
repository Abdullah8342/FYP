from django.db import models
from django.contrib.auth.models import User
from Booking.models import Booking
from django.core.exceptions import ValidationError
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,related_name='review')
    rating = models.PositiveIntegerField(default=3)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.booking}'

    def clean(self):
        if self.rating <= 0 or self.rating > 5:
            raise ValidationError('Rating is in Range 1 to 5')

        if self.user == self.booking.helper_service.user:
            raise ValidationError('You Can Not Comment On Your Service')


        if not self.booking.status == 'Completed':
            raise ValidationError('Comment Only When The Task is Completed')


        if self.user != self.booking.user:
            raise ValidationError('You Dont have Permissions For Comments')


        return super().clean()
