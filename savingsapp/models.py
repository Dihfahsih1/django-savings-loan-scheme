from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    atte =(('Present','Present'),('Absent','Absent'))
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True,blank=True, null=True)
    telephone = models.IntegerField(default=0, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    application_fee = models.IntegerField(default=10000, blank=True, null=True)
    date = models.DateField(blank=False, null=True)
    status = models.CharField(max_length=123, blank=True, null=True, choices=atte, default='Present')
    social_fund = models.IntegerField(default=1000, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)
