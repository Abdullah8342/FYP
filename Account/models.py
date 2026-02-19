from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLL_CHOICES = [("SP","Service Provider"),("SA","Service Acquire")]
    roll = models.CharField(max_length=50,choices=ROLL_CHOICES,default='Service Acquire')

    def get_full_name(self):
        return super().get_full_name()
