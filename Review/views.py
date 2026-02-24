from django.conf import settings
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrIsAdminOrReadOnly
from .serializers import ReviewSerializers
from .models import Review

User = settings.AUTH_USER_MODEL


# Create your views here.
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class ReviewUpdateDestroy(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrIsAdminOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
