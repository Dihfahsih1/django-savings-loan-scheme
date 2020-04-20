from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
class CustomUser(AbstractUser):

    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True,blank=True, null=True)
    telephone = models.IntegerField(default=0, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    application_fee = models.IntegerField(default=10000, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)

class Attendance(models.Model):
    today = datetime.now()
    years=today.year
    atte =(('Present','Present'),('Absent','Absent'))
    full_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(blank=False, null=True)
    status = models.CharField(max_length=123, blank=True, null=True, choices=atte, default='Present')
    social_fund = models.IntegerField(default=1000, blank=True, null=True)
    attendance_year = models.CharField(max_length=255, blank=True, null=True, default=years)
    attendance_month = models.CharField(max_length=255, blank=True, null=True)
class LookUps(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    def __str__(self):
        return self.name

class LookupsDetails(models.Model):
    lookup_name =  models.ForeignKey(LookUps, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    details = models.CharField(max_length=255, blank=False, null=False, unique=True)
    def __str__(self):
        return self.details
