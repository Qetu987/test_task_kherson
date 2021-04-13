from annoying.decorators import render_to
from items.models import Item
from sales.models import Sale
from .form import SaleForm
import datetime
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator


"""
рендерим главную страницу
передаем туда список товаров и по флагам уже разбиваем внутри шаблона на разные карусели и главный товар
ну и передаем время 
"""


@render_to("index.html")
def index(request):
    items = Item.objects.all()
    top_item = Item.objects.filter(is_top_item=True)
    date_of_gen = datetime.datetime.now()
    return {"items": items, "top_item": top_item[0], "date": date_of_gen}


"""
рендерим страницу каталога 
передаем туда список товаров и с помощью js отображаем по строкам, так как магаз у нас маленький, нет смысла отображать по многу
ну и передаем время 
"""


@render_to("catalog.html")
def catalog(request):
    items = Item.objects.all()
    date_of_gen = datetime.datetime.now()
    return {"items": items, "date": date_of_gen}


"""
рендерим страницу конкретного товара 
передаем туда товар и кидаем форму для заполнения таблицы продаж
ну и передаем время 
"""


@render_to("item_detail.html")
def item_detail(request, slug):
    item = Item.objects.get(title=slug)
    items = Item.objects.all()
    date_of_gen = datetime.datetime.now()

    if request.method == "POST":
        sale_form = SaleForm(data=request.POST)
        if sale_form.is_valid():
            new_sale = sale_form.save(commit=False)
            new_sale.item = item
            new_sale.save()
            return HttpResponseRedirect("/")
    else:
        sale_form = SaleForm()

    return {
        "item": item,
        "items": items,
        "sale_form": sale_form,
        "date": date_of_gen,
    }


"""
рендерим страницу продаж 
так как она видна всем (авторизированым на кнопочку, а хитрым простым юзерам по ссылке)
дальнейшее отображение контента делится на 2 этапа:
        - показать все продажи если есть авторизация
        - попросить пользователя авторизироваться
ну и передаем время 
"""


@render_to("sales.html")
def sales(request):
    sales = Sale.objects.all().order_by("-date")
    date_of_gen = datetime.datetime.now()

    sales_paginator = Paginator(sales, 5)
    page_num = request.GET.get("page")
    page = sales_paginator.get_page(page_num)

    return {"page": page, "date": date_of_gen}


"""
рендерим страницу изменения товара
передаем туда товар и кидаем форму для изменения цены
ну и передаем время 
"""


@render_to("change.html")
def change(request, slug):
    item = Item.objects.get(title=slug)
    date_of_gen = datetime.datetime.now()

    if request.method == "POST":
        history_form = SaleForm(data=request.POST)
        if history_form.is_valid():
            new_sale = history_form.save(commit=False)
            new_sale.item = item
            new_sale.save()

    else:
        sale_form = SaleForm()

    return {"item": item, "sale_form": sale_form, "date": date_of_gen}
