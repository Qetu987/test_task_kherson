from django.test import TestCase
import requests


# Create your tests here.
class Path_test(TestCase):
    def test_main_url(self):
        url = 'http://127.0.0.1:8000/'
        req = requests.get(url)
        self.assertEquals(200, req.status_code)