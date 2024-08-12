from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from django.conf import settings
from authservice.models import User
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from django.contrib.auth import authenticate
# Create your views here.
# User= settings.AUTH_USER_MODEL
# print(User)

class UserRegistration(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            # "user": UserSerializer(user).data,
            "message": "User registered successfully!"
        }, status=status.HTTP_201_CREATED)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Generate JWT token pair
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)