from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import StudentRegisterSerializer, StudentLoginSerializer
from rest_framework import response
from rest_framework import status
# from django.auth import authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class StudentRegisterView(GenericAPIView):
    serializer_class = StudentRegisterSerializer
    def post(self, request):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status = status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = StudentLoginSerializer

