from rest_framework import serializers
from django.contrib.auth import get_user_model
from Booking.models import Booking
from .models import Review

User = get_user_model()


class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )
    user_profile = serializers.HyperlinkedRelatedField(
        view_name="profile-view",
        source="user.profile",
        queryset = User.objects.all()
    )
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all())
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "user_profile",
            "booking",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
