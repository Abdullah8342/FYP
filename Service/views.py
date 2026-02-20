from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly
from .serializers import ServiceSerializers
from .models import Service

# Create your views here.


class ServiceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
