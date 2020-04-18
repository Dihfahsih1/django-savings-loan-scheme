from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField

class addmemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','telephone','first_name','last_name','application_fee')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('date','name','status','social_fund')
