from django.contrib import admin
from .models import Item, History_of_price


"""
админка для товара 
"""


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "desc",
        "curent_sale",
        "is_active",
        "is_first_carusel",
        "is_second_carusel",
    ]
    list_display_links = ["id", "title"]
    search_fields = ["id", "title", "curent_sale", "is_active"]


"""
админка для истории цен
"""


@admin.register(History_of_price)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "price", "date"]
    list_display_links = ["id", "item"]
    search_fields = ["id", "item", "date"]
