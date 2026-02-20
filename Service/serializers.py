from rest_framework import serializers
from .models import Service


class ServiceSerializers(serializers.ModelSerializer):
    description = serializers.CharField(required = False)
    class Meta:
        model = Service
        fields = ['id','name','description']
        read_only_fields = ['id']
