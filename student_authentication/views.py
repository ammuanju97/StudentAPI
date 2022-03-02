from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import response
from rest_framework import status
from .serializers import StudentRegisterSerializer, StudentLoginSerializer


# Student Registration View
class StudentRegisterView(GenericAPIView):
    serializer_class = StudentRegisterSerializer
    def post(self, request):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status = status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# student login view
class StudentLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = StudentLoginSerializer
