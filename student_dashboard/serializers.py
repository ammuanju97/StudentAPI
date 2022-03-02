from rest_framework import serializers
from .models import StudentProfile

# Student Profile serializer
class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'image', 'DOB', 'address')
        