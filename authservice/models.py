from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(_("email_address"), max_length=254, unique=True, null=False)
    username = models.CharField(_("username"), max_length=50, unique=True, null=False)
    Gender = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField(_("first name"), max_length=254, null=False)
    last_name = models.CharField(_("last name"), max_length=254, null=False)
    date_of_birth = models.DateField(_("Date of Birth"), max_length=10, null=False)
    gender = models.CharField(_("gender"), max_length=16, choices=Gender, blank=True)
    age = models.IntegerField(_("age"), max_length=254, null=False)
    bio = models.TextField(_("bio data"), max_length=1024,)

    