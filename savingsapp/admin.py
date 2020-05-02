from django.contrib import admin
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
class CustomUser(admin.ModelAdmin):
    list_display = ('full_name','total_saving')

admin.site.register(Attendance)
admin.site.register(SavingCycle)
admin.site.register(Saving)
admin.site.register(Loan)