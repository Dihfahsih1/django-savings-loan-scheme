from django.contrib import admin
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
class CustomUser(admin.ModelAdmin):
    list_display = ('full_name')
