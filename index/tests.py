from django.test import TestCase
import requests
from items.models import Item
from sales.models import Sale
from seller.models import User


# Create your tests here.
class Path_test(TestCase):

    """
    создаем тестовые экзкмпляры
    """

    def setUp(self):
        self.user = User.objects.create(username="testuser", password="test")
        self.item = Item.objects.create(
            title="testitem", desc="test", curent_sale="200", is_active=True
        )
        self.sale = Sale.objects.create(user=self.user, item=self.item, count=20)

    """
    тесты на доступность страниц
    """

    def test_main_url(self):
        url = "http://127.0.0.1:8000/"
        req = requests.get(url)
        self.assertEquals(200, req.status_code)

    def test_catalog_url(self):
        url = "http://127.0.0.1:8000/catalog/"
        req = requests.get(url)
        self.assertEquals(200, req.status_code)
