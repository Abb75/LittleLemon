from django.test import TestCase
from ..models import Menu, Booking

class MenuItemTest(TestCase):
      def test_get_item(self):
       
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")

      def test_booking(self):
       
        item = Booking.objects.create(name="Alex", nb_of_guest=80)
        self.assertEqual(item.name, "Alex")

