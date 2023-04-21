from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import json

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Salad", price=10, inventory=3)

    def test_getall(self):
        client = APIClient()
        response = client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serialized_data = json.loads(json.dumps(menus.values()))
        # Check if serialized data equals response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_data)