from django.contrib.auth.models import User
from .serializers import StudentProfileSerializer
from .models import StudentProfile
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class StudentProfileView(generics.GenericAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        serializer = StudentProfileSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = StudentProfile.objects.create(
                user = request.user,
                image = serializer.validated_data['image'],
                DOB = serializer.validated_data['DOB'],
                address = serializer.validated_data['address']
            )
            user.save()
            data['message'] = 'Profile fields added sucessfully'
        else:
            data = serializer.errors
            return Response(data, status = status.HTTP_400_BAD_REQUEST)
        return Response(data, status = status.HTTP_201_CREATED)