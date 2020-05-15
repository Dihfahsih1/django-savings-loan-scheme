from django.contrib import admin
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
class CustomUser(admin.ModelAdmin):
    list_display = ('full_name', 'total_saving',
                    'maximum_loan_amount', 'total_social_fund')

admin.site.register(Loan)
class Loan(admin.ModelAdmin):
    list_display = ('Loan_Paid', 'balance', 'status')


admin.site.register(SocialFund)
admin.site.register(Attendance)
admin.site.register(Cycle)
admin.site.register(Saving)
admin.site.register(PayingLoan)
admin.site.register(Stock)
