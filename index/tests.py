from django.test import TestCase
import requests
from index.views import Item


# Create your tests here.
class Path_test(TestCase):
    def setUp(self):
        self.test_item = Item.objects.create(title="Test_item", desc="Test_desc", curent_sale="100", is_active=True)


    def test_main_url(self):
        url = 'http://127.0.0.1:8000/'
        req = requests.get(url)
        self.assertEquals(200, req.status_code)


    def test_catalog_url(self):
        url = 'http://127.0.0.1:8000/catalog/'
        req = requests.get(url)
        self.assertEquals(200, req.status_code)


    