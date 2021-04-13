from django import forms
from sales.models import Sale
from items.models import Item, History_of_price


"""
форма для создание продажи на товаре
"""


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ("user", "count")


"""
форма для изменение цены на товаре
"""


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("curent_sale",)
