from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

from api.tests.test_cart import create_pizza, create_margarita, add_meal_item_in_cart

# Create your tests here.

class UsersTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_users_management(self):
        # anonumius
        response = self.client.get(path="/api/users/", format="json")
        self.assertEqual(response.status_code, 401)

        # create a new user
        data = {
            "email"    : "super-staff@email.com",
            "username" : "super-staff",
            "password" : "longPassword+33333"
        }

        # Send a POST request to the registration endpoint
        response = self.client.post(
            "/api/users/",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        # Check if the response status code is 201 Created

        self.assertEqual(response.status_code, 201)

        my_user = User.objects.all().filter(username = 'super-staff')
        my_user.is_staff = True
        my_user.is_superuser = True
        my_user.is_active = True

        # get token
        response = self.client.post(
            path = "/token/login",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

        # login as staff user
        self.user = my_user
        self.client.login(username='super-staff', password='longPassword+33333')

        # check again
        response = self.client.get(path="/api/users/", format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, response.data['count'])

        # check myself
        response = self.client.get(path="/api/users/me/", format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'super-staff')
