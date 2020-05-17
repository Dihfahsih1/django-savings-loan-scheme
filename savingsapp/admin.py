from django.contrib import admin
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
class CustomUser(admin.ModelAdmin):
    list_display = ('full_name', 'total_saving',
                    'maximum_loan_amount', 'total_social_fund')


admin.site.register(PayingLoan)


class PayingLoan(admin.ModelAdmin):
    list_display = ('total_repayment')
admin.site.register(Loan)
admin.site.register(SocialFund)
admin.site.register(Attendance)
admin.site.register(Cycle)
admin.site.register(Saving)
admin.site.register(Stock)
