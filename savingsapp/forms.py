from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput

class MemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','telephone','first_name','last_name','application_fee','date','status','social_fund')
