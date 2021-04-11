from annoying.decorators import render_to
from items.models import Item
from .form import SaleForm


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
            print(new_sale)
            new_sale.save()
    else:
        sale_form = SaleForm()
        print('dodya')

    return {'item': item,
            'items': items,
            'sale_form': sale_form}