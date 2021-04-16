from django.test import TestCase
import requests
from items.models import Item, History_of_price
from sales.models import Sale
from seller.models import User
from django.urls import reverse



# Create your tests here.
class Path_test(TestCase):

    """
    создаем тестовые экзкмпляры
    """

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

        number_of_items = 13
        for item_num in range(number_of_items):
            Item.objects.create(
                title='item %s' % item_num, 
                desc = 'Surname %s' % item_num, 
                curent_sale = item_num,
                is_active = True,
                is_first_carusel = True,
                is_second_carusel = True,
                is_top_item = True,
                )

            sale = Sale.objects.create(
                user = test_user1,
                item = Item.objects.get(id=1),
                count = 1
            )
        

        

    """
    тесты на доступность страниц
    """

    def test_main_url(self):
        resp = self.client.get(reverse(''))
        self.assertEqual(resp.status_code, 200)

    def test_catalog_url(self):
        resp = self.client.get(reverse('catalog'))
        self.assertEqual(resp.status_code, 200)

    def test_sales_url(self):
        resp = self.client.get(reverse('sales'))
        self.assertEqual(resp.status_code, 200)

    '''
    Тест на предметы внутри каталога
    '''
    def test_items_in_page_catalog(self):
        resp = self.client.get(reverse('catalog'))
        self.assertTrue( len(resp.context['items']) >= 0)

    '''
    Тест на предметы внутри гл страницы
    '''   
    def test_items_in_page_main(self):
        resp = self.client.get(reverse(''))
        self.assertTrue( len(resp.context['items']) >= 13)


    '''
    Тест на создание чего-то в контекст процессоре
    '''
    def test_items_in_page_mainFoo(self):
        resp = self.client.get(reverse(''))
        self.assertTrue( resp.context['date'] != '')


    def test_logged(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('sales'))

        ''' авторизировались ли мы '''
        self.assertEqual(str(resp.context['user']), '<User testuser1 />')
        ''' видит ли пользователь нашу страницу '''
        self.assertEqual(resp.status_code, 200)
        ''' сколько записей отображается на первой странице '''
        self.assertTrue( len(resp.context['page']) == 5)

    def test_item_detale(self):
        item = Item.objects.get(id=1)
        self.assertEquals(item.get_absolute_url(),'/catalog/1')
        resp = self.client.get(item.get_absolute_url())
        self.assertEqual(resp.status_code, 200)


    def test_history_of_price(self):
        history = History_of_price.objects.all()
        self.assertTrue( len(history) >= 13)

    
    def test_test_of_price(self):
        Item.objects.create(
                title='item_tets_for_history', 
                desc = 'Surname', 
                curent_sale = 222,
                is_active = True,
                is_first_carusel = True,
                is_second_carusel = True,
                is_top_item = True,
                )
        
        item = Item.objects.get(title='item_tets_for_history')
        history = History_of_price.objects.get(item=item)
        self.assertTrue( history.price == item.curent_sale)