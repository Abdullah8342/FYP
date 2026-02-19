from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers
from .models import User
# Create your views here.
class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class LogoutView(APIView):
    def post(self,request):
        serializers = TokenBlacklistSerializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        return Response({"message":"Logout Successfuly"})
