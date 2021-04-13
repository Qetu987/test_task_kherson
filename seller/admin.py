from django.contrib import admin
from .models import User

"""
админка для юзвера
"""
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "last_login"]
    list_display_links = ["id", "username"]
    search_fields = ["id", "username"]
