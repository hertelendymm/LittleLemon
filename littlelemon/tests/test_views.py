from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

        Menu.objects.create(id=11,title="Coffee", price=80, inventory=101)
        Menu.objects.create(id=12,title="IceCream", price=80, inventory=102)

    def test_getall(self):
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data) 
    