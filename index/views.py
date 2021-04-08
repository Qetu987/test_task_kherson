from annoying.decorators import render_to
from  items.models import Item


@render_to('index.html')
def index(request):
    return {'data': 'data'}


@render_to('catalog.html')
def catalog(request):
    items = Item.objects.all()
    return {'items': items}