from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput


class MemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','telephone','first_name','last_name','application_fee')

class CyclesForm(forms.ModelForm):
    class Meta:
        model=Cycles
        fields=('cycle_name','cycle_period_start','cycle_period_end')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('full_name','date','status','social_fund')
        status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

class SavingsForm(forms.ModelForm):
    class Meta:
        model=Saving
        fields=('name','cycle','date','amount')