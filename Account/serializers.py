from rest_framework import serializers
from Helper.models import HelperService
from Service.models import Service
from .models import User


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), required=False, write_only=True
    )
    first_name = serializers.CharField(required=True, max_length=100)
    last_name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "roll",
            "service",
            "password",
            "password1",
        ]
    def validate(self, attrs):
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError("password and conform password not same")
        if attrs["roll"] == "SP":
            if not "service" in attrs:
                raise serializers.ValidationError("Services Are Not Selected")
        if attrs["roll"] == "SA":
            if "service" in attrs:
                raise serializers.ValidationError(
                    "Please Change The Roll To SP (Service Provider) Or Remove Services"
                )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password1")
        try:
            print("Try Block In Account Serializers.py")
            service = validated_data.pop("service")
            user = User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
            HelperService.objects.create(user=user, service=service)
        except Exception:
            print("Except Block In Account Serializers.py")
            user = User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
        return user
