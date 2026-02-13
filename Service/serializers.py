from rest_framework import serializers
from .models import Service


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name','description']
        read_only_fields = ['id','name','description']
