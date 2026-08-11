from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Category, Cuisine, Meal

# Create your tests here.

def create_pizza():
    # create Category
    category = Category.objects.create(
        title = "Main"
    )
    # create Cuisine
    cuisine = Cuisine.objects.create(
        name = "Italian"
    )
    # create Meal
    pizza = Meal.objects.create(
        name = "Pizza",
        cuisine = cuisine,
        category = category,
        price = 10.00,
        desc = 'Original pizza',
        image = '/static/path_to_image/pizza.jpg',
        image_text = 'Pizza'
    )
    return pizza

def create_margarita():
    # create Category
    category = Category.objects.create(
        title = "Drink"
    )
    # create Cuisine
    cuisine = Cuisine.objects.create(
        name = "Italian"
    )
    # create Meal
    margarita = Meal.objects.create(
        name = "Margarita",
        cuisine = cuisine,
        category = category,
        price = 7.50,
        desc = 'Original Margarita',
        image = '/static/path_to_image/margarita.jpg',
        image_text = 'Margarita'
    )
    return margarita

def add_meal_item_in_cart(user, client, item_count, item):
    data = {
        "user_id" : user.id,
        "meal_id" : item.id,
        "count" : item_count,
        "unit_price" : item.price,
        "price" : item_count * item.price,
    }
    response = client.post(
        path = "/api/cart/menu-items",
        data = data,
        format = "json",
        headers = {'Content-Type': 'application/json'}
    )
    return response

class CartTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin@admin.com',
            password='admin'
        )

    def test_cart_no_auth(self):
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 401)

    def test_cart_post_get_delete_with_auth(self):
        self.client.login(username='admin@admin.com', password='admin')

        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        # Cart is empty
        cart = response.data
        self.assertEqual(0, cart['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 2, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 2, margarita)
        self.assertEqual(response.status_code, 201)

        # Cart is NOT empty
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)
        cart = response.data
        self.assertEqual(2, cart['count'])

        response = self.client.delete(path="/api/cart/menu-items")
        self.assertEqual(response.status_code, 204) # deleted

        response = self.client.delete(path="/api/cart/menu-items")
        self.assertEqual(response.status_code, 204) # deleted

        # Cart is empty again
        response = self.client.get(path="/api/cart/menu-items", format="json")
        self.assertEqual(response.status_code, 200)
        cart = response.data
        self.assertEqual(0, cart['count'])
