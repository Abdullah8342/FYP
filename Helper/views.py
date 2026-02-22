from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import HelperService, Location
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import HelperServiceSerializers, LocationSerializers


# Create your views here.
class LocationViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


class HelperServiceViewset(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = (
        HelperService.objects.all()
        .select_related("service")
        .prefetch_related("location")
    )
    serializer_class = HelperServiceSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
