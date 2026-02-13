from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .serializers import BookingSerializers
from .models import Booking


# Create your views here.
class BookingView(APIView):

    def get(self, request):
        queryset = Booking.objects.filter(user=request.user)
        serializers = BookingSerializers(
            queryset, many=True, context={"request": request}
        )
        return Response(serializers.data)

    def post(self, request):
        serializers = BookingSerializers(
            data=request.data, context={"request": request}
        )
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_201_CREATED)


class BookingDetailsView(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Booking, id=pk)
        serializers = BookingSerializers(queryset, context={"request": request})
        return Response(serializers.data)

    def patch(self, request, pk):
        queryset = get_object_or_404(Booking, id=pk)
        serializers = BookingSerializers(
            queryset, data=request.data, context={"request": request}
        )
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_200_OK)

    def delete(self, request, pk):
        queryset = get_object_or_404(Booking, id=pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)
