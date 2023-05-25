from django.test import TestCase
from ..models import Menu
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from ..serializers import UserSerializer, MenuSerializer
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from ..views import MenuItemsView

class MenuTestView(TestCase):

        def setUp(self):
            self.factory = APIRequestFactory()

            #self.client = APIClient()
            self.url = '/menu-view/'
            self.obj =Menu.objects.create(title="IceCream", price=80, inventory=100)
            self.user = User.objects.create_user(username='testuser', password='testpassword')


        def test_get_all_menu(self):
            request = self.factory.get(self.url)
            force_authenticate(request, user=self.user)  # Authentification forcée
            view = MenuItemsView.as_view()
            response = view(request)
            serializer = MenuSerializer(self.obj, context={'request': response})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, serializer.data)
