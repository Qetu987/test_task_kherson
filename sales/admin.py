from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "item", "count", "date"]
    list_display_links = ["id", "user"]
    search_fields = ["id", "user", "item", "date"]