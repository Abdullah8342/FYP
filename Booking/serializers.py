from rest_framework import serializers
from django.contrib.auth import get_user_model
from Helper.models import HelperService
from Helper.serializers import HelperServiceSerializers
from .models import Booking

User = get_user_model()


class BookingSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    helper_service_id = serializers.PrimaryKeyRelatedField(
        queryset=HelperService.objects.all(),
        write_only=True,
        source="helper_service"
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
