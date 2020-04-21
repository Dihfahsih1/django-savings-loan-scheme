from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput
from django.forms import formset_factory
class MemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','telephone','first_name','last_name','application_fee')
class LookUpsForm(forms.ModelForm):
    class Meta:
        model=LookUps
        fields=('name',)

class LookUpsDetailsForm(forms.ModelForm):
    class Meta:
        model=LookupsDetails
        fields=('lookup_name','details',)

class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields='__all__'
        widgets = {
            'date': DatePickerInput(),

        }
AttendanceFormset=formset_factory(AttendanceForm),
