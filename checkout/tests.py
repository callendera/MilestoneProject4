from django.test import TestCase
from .models import Order


class OrderTests(TestCase):
    """
    Tests run against order model
    """

    def test_str(self):
        test_user = Order(user='An order')
        self.assertEqual(str(test_user), 'An order')
