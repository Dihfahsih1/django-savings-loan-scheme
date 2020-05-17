from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput


class MemberForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields = ('status', 'email', 'telephone', 'first_name', 'last_name',
                  'application_fee', 'is_active', 'is_staff', 'is_superuser', 'Role',)


class SocialFundForm(forms.ModelForm):
    class Meta:
        model = SocialFund
        fields = ('full_name','social_fund', 'date')

class CyclesForm(forms.ModelForm):
    class Meta:
        model=Cycle
        fields=('cycle_name','cycle_period_start','cycle_period_end','rate','is_active')


class EditCycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = ('cycle_name', 'cycle_period_start',
                  'cycle_period_end', 'rate')
        widgets = {
            'date': TextInput(attrs={'placeholder': 'Date(YYY-MM-DD)'})
        }
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('full_name','date','status')
        status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

class SavingsForm(forms.ModelForm):
    class Meta:
        model=Saving
        fields=('name','date','amount')

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields = ('name', 'date', 'amount', 'interest_rate',
                  'loan_period', 'recorded_by', 'loan_status')
                  
class PayingLoanForm(forms.ModelForm):
    class Meta:
        model=PayingLoan
        fields = ('loan_id', 'name', 'date', 'amount')

class EditLoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields = ('name', 'date', 'amount', 'interest_rate',
                  'loan_period', 'loan_status')
        labels = {
            'date': 'Date (YYY-MM-DD)'
        }
class LookupForm(forms.ModelForm):
    class Meta:
        model=LookUp
        fields=('name',)

class LookupDetailsForm(forms.ModelForm):
    class Meta:
        model=LookupDetail
        fields=('Lookup_Name','Details')
