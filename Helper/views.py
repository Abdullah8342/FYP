from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import HelperService,Location
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from .serializers import HelperServiceSerializers,LocationSerializers


# Create your views here.
class LocationViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly,permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


class HelperServiceViewset(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = HelperService.objects.all()
    serializer_class = HelperServiceSerializers
