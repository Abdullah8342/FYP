from rest_framework.views import APIView
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.response import Response
from .serializers import ProfileSerializers
from django.shortcuts import get_object_or_404
from .models import Profile
# Create your views here.
class ProfileView(APIView):
    def get(self,request):
        queryset = get_object_or_404(Profile,user = request.user)
        serializers = ProfileSerializers(queryset)
        return Response(serializers.data)

    def patch(self,request):
        queryset = get_object_or_404(Profile,user = request.user)
        serializers = ProfileSerializers(
            queryset,data = request.data,
            context = {'request':request}
        )
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_202_ACCEPTED)


class ProfileDetailsView(APIView):
    def get(self,request,pk):
        queryset = get_object_or_404(Profile,user = pk)
        serializers = ProfileSerializers(queryset)
        return Response(serializers.data)