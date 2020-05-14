from django.test import TestCase
from .models import Product
from django.urls import reverse, resolve
from .views import all_products


class TestProductUrls(TestCase):
    """
    Tests run against product url
    """
    def test_url_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, all_products)


class ProductTests(TestCase):
    """
    Tests run against product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
