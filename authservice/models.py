from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email_address", max_length=254, unique=True, null=False)
    username = models.CharField("username", max_length=50, unique=True, null=False)
    Gender = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField("first name", max_length=254, null=True)
    last_name = models.CharField("last name", max_length=254, null=True)
    date_of_birth = models.DateField("Date of Birth", max_length=10, null=True)
    gender = models.CharField("gender", max_length=16, choices=Gender, blank=True)
    age = models.IntegerField("age", null=True)
    bio = models.TextField("bio data", max_length=1024,)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    

    