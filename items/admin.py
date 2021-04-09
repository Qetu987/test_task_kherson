from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "desc", "curent_sale", "is_active", "image_tag", 'is_first_carusel', 'is_second_carusel']
    list_display_links = ["id", "title"]
    search_fields = ["id", "title", "curent_sale", "is_active"]