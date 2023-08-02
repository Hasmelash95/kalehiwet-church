from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    The view on the admin site for the Profile model
    """
    list_display = ('first_name', 'last_name', 'role', 'created_on')


