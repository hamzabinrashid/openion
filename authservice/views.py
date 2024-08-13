# DjanoRestFramwork
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# DJango services
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

# First Party
from authservice.serializers import CustomTokenObtainPairSerializer, UserSerializer
from authservice.models import User
from authservice.utilities.authentication import authenticate, get_token
import requests

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        tokens = get_token(user)
        return Response({
            **tokens,
            "message": "User registered successfully!"
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserLogin(APIView):
    queryset = User.objects.all()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # user = get_object_or_404(User, email=email)

        auth, status = authenticate(email=email, password=password)

        return Response(auth, status=status)


        if user is not None:
            # Generate JWT token pair
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
