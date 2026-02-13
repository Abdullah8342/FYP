from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()

class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    profile_picture = serializers.CharField(required = False)
    class Meta:
        model = Profile
        fields = ['id','user','full_name','profile_picture','phone']
        read_only_fields = ['id']
