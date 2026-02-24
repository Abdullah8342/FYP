from rest_framework import serializers
from django.conf import settings
from Booking.models import Booking
from .models import Review

User = settings.AUTH_USER_MODEL


class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only = True
    )
    booking = serializers.PrimaryKeyRelatedField(write_only = True,queryset = Booking.objects.all())
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "booking",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
