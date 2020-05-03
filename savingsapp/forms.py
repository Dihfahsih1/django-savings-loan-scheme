from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput


class MemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','telephone','first_name','last_name','application_fee','is_active','is_staff','is_superuser', 'Role')

class CyclesForm(forms.ModelForm):
    class Meta:
        model=SavingCycle
        fields=('cycle_name','cycle_period_start','cycle_period_end','interest_rate','is_active','archive_status')
        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('full_name','date','status','social_fund')
        status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

class SavingsForm(forms.ModelForm):
    class Meta:
        model=Saving
        fields=('name','cycle','date','amount')

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields= ('name','cycle','date','amount','interest_rate', 'loan_period','recorded_by','is_loanee')
class PayingLoanForm(forms.ModelForm):
    class Meta:
        model=PayingLoan
        fields=('loan_id','name','date','amount')

class EditLoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields=('name','date','amount','interest_rate','loan_period','is_loanee')        