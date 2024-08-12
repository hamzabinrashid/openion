from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    path('register/', views.UserRegistration, name='register'),
    path('token/', views.CustomTokenObtainPairView, name='token_obtain_pair'),
    
]
