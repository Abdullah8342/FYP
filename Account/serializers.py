from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    password1 = serializers.CharField(write_only = True)
    service_list = serializers.ListField(required = False,write_only = True)
    first_name = serializers.CharField(required = True,max_length = 100)
    last_name = serializers.CharField(required = True,max_length = 100)
    email = serializers.EmailField(required = True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "roll",
            'service_list',
            "password",
            "password1",
        ]
    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError('password and conform password not same')
        if attrs['roll'] == 'SP':
            if not 'service_list' in attrs:
                raise serializers.ValidationError('Services Are Not Selected')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password1')
        try:
            service_list = validated_data.pop('service_list')
            print(service_list)
        except Exception:
            print("service_list Not Provided")
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
