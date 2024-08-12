from typing import Any, Dict
from rest_framework import serializers
# from django.conf import settings
from authservice.models import User 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['email','password', 'username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'age']
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user']= UserSerializer(self.user).data
        return data
  