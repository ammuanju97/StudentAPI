from rest_framework import serializers
from .models import StudentProfile, StudentMarkDetails

# Student Profile serializer
class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'image', 'DOB', 'address')
        

# Student mark details serializer
class StudentMarkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarkDetails
        fields = ('id', 'english_mark', 'maths_mark', 'science_mark', 'malayalam_mark',
                 )
                