from annoying.decorators import render_to
from items.models import Item


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
    return {'items': item}