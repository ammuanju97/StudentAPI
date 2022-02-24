from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 128, min_length = 3, write_only = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(StudentLoginSerializer, cls).get_token(user)
        return token

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({'message':
                ('A user with this email and password is not found.')}
            )

        return super().validate(attrs)