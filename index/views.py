from annoying.decorators import render_to
from items.models import Item
from sales.models import Sale
from .form import SaleForm

from django.core.paginator import Paginator


@render_to('index.html')
def index(request):
    items = Item.objects.all()
    top_item = Item.objects.filter(is_top_item = True)
    return {'items': items, 'top_item': top_item[0]}


@render_to('catalog.html')
def catalog(request):
    items = Item.objects.all()
    return {'items': items}


@render_to('item_detail.html')
def item_detail(request, slug):
    item = Item.objects.get(title=slug)
    items = Item.objects.all()
    
    if request.method == 'POST':
        sale_form = SaleForm(data=request.POST)
        if sale_form.is_valid():
            new_sale = sale_form.save(commit=False)
            new_sale.item = item
            new_sale.save()
    else:
        sale_form = SaleForm()

    return {'item': item,
            'items': items,
            'sale_form': sale_form}


@render_to('sales.html')
def sales(request):
    sales = Sale.objects.all().order_by('-date')

    sales_paginator = Paginator(sales, 5)
    page_num = request.GET.get('page')
    page = sales_paginator.get_page(page_num)

    return {
        'page': page,
        }