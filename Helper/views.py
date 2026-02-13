from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from .serializers import HelperServiceSerializers
from .models import HelperService


# Create your views here.
class HelperServiceView(APIView):

    def get(self, request):
        queryset = HelperService.objects.filter(user=request.user)
        serializers = HelperServiceSerializers(
            queryset, many=True, context={"request": request}
        )
        return Response(serializers.data)

    def post(self, request):
        serializers = HelperServiceSerializers(
            data=request.data, context={"request": request}
        )
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_201_CREATED)


class HelperServiceDetailsView(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(HelperService, id=pk)
        serializers = HelperServiceSerializers(queryset)
        return Response(serializers.data)

    def patch(self, request, pk):
        queryset = get_object_or_404(HelperService, id=pk)
        serializers = HelperServiceSerializers(
            queryset, data=request.data, context={"request": request}
        )
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_200_OK)

    def delete(self, request, pk):
        queryset = get_object_or_404(HelperService, id=pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)
