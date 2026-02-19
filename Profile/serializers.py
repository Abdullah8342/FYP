from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )
    full_name = serializers.CharField(
        max_length=120, read_only=True, source="user.get_full_name"
    )
    email = serializers.EmailField(source="user.email", read_only=True)
    # service
    profile_picture = serializers.ImageField(required = False)
    phone = serializers.CharField(required=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "full_name", "email", "profile_picture", "phone"]
        read_only_fields = ["id","user","full_name","email"]
