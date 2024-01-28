from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, blank=True, unique=True)
    password = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)

