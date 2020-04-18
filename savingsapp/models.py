from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True,blank=True, null=True)
    telephone = models.IntegerField(default=0, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    application_fee = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
