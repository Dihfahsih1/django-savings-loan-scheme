from django.contrib import admin
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
class CustomUser(admin.ModelAdmin):
    list_display = ('full_name')

admin.site.register(Attendance)
admin.site.register(LookUps)
admin.site.register(LookupsDetails)
admin.site.register(Saving)