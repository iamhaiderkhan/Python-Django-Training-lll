from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import CustomUser
from .forms import CustomUserForm

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):

    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_superuser', 'is_active', 'is_staff']
    list_display = ['username', 'email', 'first_name', 'last_name','is_superuser', 'is_active', 'is_staff']

    form = CustomUserForm


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)


