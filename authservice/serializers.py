from typing import Any, Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    model=User
    fields = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'age', 'bio']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user']= UserSerializer(self.user).data
        return data
  