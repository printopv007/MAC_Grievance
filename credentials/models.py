from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField( max_length=30, null=True, blank=True)

