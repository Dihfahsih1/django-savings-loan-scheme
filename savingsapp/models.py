from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.db.models import Sum

class CustomUser(AbstractUser):
	roles =(('Admin','Admin'),('Ordinary','Ordinary'))
	email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
	username = models.CharField(max_length=30, unique=True,blank=True, null=True)
	telephone = models.IntegerField(default=0, blank=True, null=True)
	first_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	username = models.CharField(max_length=30, unique=True, blank=True, null=True)
	application_fee = models.IntegerField(default=10000, blank=True, null=True)
	Role = models.CharField(max_length=250, choices=roles)
	is_active = models.BooleanField(default=True)   # can login
	is_staff = models.BooleanField(default=False)  # staff user non superuser
	is_superuser = models.BooleanField(default=False)
	USERNAME_FIELD = 'username'
	REQUIRED_FILEDS = []
	def __str__(self):
		return str(self.first_name)  + ' ' + str(self.last_name)
	@property 
	def total_saving(self):
		cycles = SavingCycle.objects.filter(is_active=True)
		for i in cycles:
			startdate= i.cycle_period_start
			enddate= i.cycle_period_end
			results=Saving.objects.filter(date__range=(startdate, enddate),name=self.id).aggregate(totals=models.Sum("amount"))
			if (results['totals']):
				return results["totals"]
			else:
				return 0 

	@property
	def maximum_loan_amount(self):
		cycles = SavingCycle.objects.filter(is_active=True)
		for i in cycles:
			startdate = i.cycle_period_start
			enddate = i.cycle_period_end
			results = Saving.objects.filter(date__range=(
					startdate, enddate), name=self.id).aggregate(totals=models.Sum("amount"))
			if (results['totals']):
				x=(results["totals"]*2)
				return x
			else:
				return 0
	@property
	def full_name(self):
		return str(self.first_name) + ' ' + str(self.last_name)

class Attendance(models.Model):
	today = datetime.now()
	years=today.year
	atte =(('Present','Present'),('Absent','Absent'))
	full_name = models.CharField(max_length=123, null=True, blank=True)
	date = models.DateField(blank=True, null=True)
	status = models.BooleanField(blank=True, default=False)
	social_fund = models.IntegerField(default=0, blank=True, null=True)
	attendance_year = models.CharField(max_length=255, blank=True, null=True, default=years)
	attendance_month = models.CharField(max_length=255, blank=True, null=True)


class SavingCycle(models.Model):
	status =(('ARCHIVED','ARCHIVED'),('UNARCHIVED','UNARCHIVED' ))
	archive_status = models.CharField(max_length=200, choices=status,blank=True, null=True)
	interest_rate =  models.IntegerField(default=5, null=True, blank=True)
	cycle_name =  models.CharField( max_length=200, null=True, blank=True, unique=True)
	cycle_period_start = models.DateField(max_length=255, blank=False, null=False, unique=True)
	cycle_period_end = models.DateField(max_length=255, blank=False, null=False, unique=True)
	is_active = models.BooleanField(default=True) 
	def __str__(self):
		return str(self.cycle_period_start) + "/" + str(self.cycle_period_end)
class Saving(models.Model):
	cycle =  models.ForeignKey(SavingCycle, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, max_length=100, null=True, blank=True)
	amount = models.IntegerField(default=0)
	def __str__(self):
		return self.name
class Loan(models.Model):
	cycle =  models.CharField(max_length=100, null=True, blank=True)
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default="kim",max_length=100, null=True, blank=True)
	amount = models.IntegerField(default=0)
	interest_rate = models.IntegerField(default=0)
	loan_period = models.IntegerField(default=0)
	is_loanee = models.BooleanField(default=True) 
	recorded_by =models.CharField(max_length=220, blank=True, null=True)
	@property
	def Loan_Paid(self):
		results = PayingLoan.objects.filter(loan_id=self.id).aggregate(totals=models.Sum("amount"))
		if (results['totals']):
			return results["totals"]
		else:
			return 0
	@property
	def balance(self):
		#Rate=self.interest_rate(0.01), 
		#I =R*P*T
		#P = self.amount
		#T = self.loan_period
		interest=((self.interest_rate /100)* self.loan_period * self.amount)
		bala = (self.amount + interest) - self.Loan_Paid
		return bala

		
	@property
	def status(self):
		
		get_id=Loan.objects.all()
		if (self.Loan_Paid > self.amount):
			for i in get_id:
				print(i.name)
			self.is_loanee = False
			return self.is_loanee
		else:
			self.is_loanee = True
			return self.is_loanee
	def __str__(self):
		return self.name

class PayingLoan(models.Model):
	loan_id = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateField(max_length=100, blank=True, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	amount = models.IntegerField(null=True, blank=True, default=0)
	def __str__(self):
		return str(self.date)

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	openn = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
	def __str__(self):
		return str(self.ticker)

class Lookup(models.Model):
	name = models.CharField(unique=True, max_length=220, blank=False, null=False)
	def __str__(self):
		return self.name

class LookupDetails(models.Model):
	Lookup_Name = models.ForeignKey(Lookup, on_delete=models.CASCADE, max_length=220, blank=False, null=False)
	Details = models.CharField(max_length=220, blank=False, null=False)
	def __str__(self):
		return self.Lookup_Name
