from django.test import TestCase
from models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(item, "Ice Cream. Price at 80. Total inventory is 100")