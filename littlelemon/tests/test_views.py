from django.test import TestCase, Client
from restaurant.models import Menu
from django.urls import reverse
import json
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Salad", Price=10, Inventory=3)

    def test_getall(self):
        client = Client()
        response = client.get(reverse('menu'))
        menus = Menu.objects.all()
        expected_data = json.dumps(list(menus.values()), cls=CustomJSONEncoder)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode()), json.loads(expected_data))