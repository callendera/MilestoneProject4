from django.test import TestCase, Client
from .views import login
from django.urls import reverse
from .models import Customer
import json


class TestloginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_login_view_POST(self):
        response = self.client.post(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html', 'base.html')
