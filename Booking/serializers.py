from rest_framework import serializers
from django.conf import settings
from Helper.models import HelperService
from Helper.serializers import HelperServiceSerializers
from .models import Booking

User = settings.AUTH_USER_MODEL


class BookingSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    helper_service_id = serializers.PrimaryKeyRelatedField(
        queryset=HelperService.objects.all(), write_only=True, source="helper_service"
    )
    helper_service = HelperServiceSerializers(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "helper_service",
            "helper_service_id",
            "status",
            "scheduled_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
