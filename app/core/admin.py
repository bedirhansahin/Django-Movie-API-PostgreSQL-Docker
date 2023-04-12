from django.contrib import admin
from . models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender', 'birth_date', 'is_active']
    search_fields = ['username']
    search_help_text = "You can search by username "
    list_filter = ['gender', 'is_active', 'is_staff']
    list_per_page = 10
    ordering = ['date_joined']
    readonly_fields = ['username', 'email']
