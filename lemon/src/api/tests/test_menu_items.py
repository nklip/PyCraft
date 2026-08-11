from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

from api.models import Category, Cuisine

# Create your tests here.

class MenuItemsTestCase(TestCase):

    def create_pizza_json(self):
        # create Category
        category = Category.objects.create(
            title = "Main"
        )
        # create Cuisine
        cuisine = Cuisine.objects.create(
            name = "Italian"
        )
        # Meal
        pizza_json = {
            "name" : "Pizza",
            "cuisine" : {"name" : cuisine.name},
            "category" : {"title" : category.title},
            "price" : '10.00',
            "desc" : 'Original pizza',
            "image" : '/static/path_to_image/pizza.jpg',
            "image_text" : 'Pizza'
        }

        return pizza_json

    def setUp(self):
        self.client = APIClient()

        self.group = Group(name = "Manager")
        self.group.save()

        self.user = User.objects.create_user(
            username='manager@manager.com',
            password='manager'
        )

    # user without a group
    def test_menu_items_as_customer(self):
        # manager is still not added in the group
        self.client.login(username='manager@manager.com', password='manager')

        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(0, cart['count'])

        pizza_json = self.create_pizza_json()

        # post
        response = self.client.post(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)

        # put
        response = self.client.put(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # patch
        response = self.client.patch(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # delete
        response = self.client.delete(
            path = "/api/menu-items",
            format = "json"
        )
        self.assertEqual(response.status_code, 403)

    # manager should be able to add new items
    def test_menu_items_as_manager_new_item(self):
        # add user in group
        self.user.groups.add(self.group)
        self.user.save()

        self.client.login(username='manager@manager.com', password='manager')

        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(0, cart['count'])

        pizza_json = self.create_pizza_json()

        # create new menu-item
        response = self.client.post(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get again
        response = self.client.get(path="/api/menu-items", format="json")
        self.assertEqual(response.status_code, 200)

        cart = response.data
        self.assertEqual(1, cart['count'])

        # put
        response = self.client.put(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # patch
        response = self.client.patch(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)
        # delete
        response = self.client.delete(
            path = "/api/menu-items",
            format = "json"
        )
        self.assertEqual(response.status_code, 403)

    # user without a group
    def test_menu_item_as_customer(self):
        # add user in manager group
        self.user.groups.add(self.group)
        self.user.save()

        # user is a manager now
        self.client.login(username='manager@manager.com', password='manager')

        pizza_json = self.create_pizza_json()

        # create new menu-item
        response = self.client.post(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get id of the created item
        id = response.data['id']
        id = id[id.rindex('/') + 1 : ]

        # remove user from manager group
        self.user.groups.remove(self.group)
        self.user.save()

        response = self.client.get(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 200)

        response = self.client.post(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 405)

        response = self.client.put(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 403)

        response = self.client.patch(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 403)

    # user without a group
    def test_menu_item_as_manager(self):
        # add user in manager group
        self.user.groups.add(self.group)
        self.user.save()

        # user is a manager now
        self.client.login(username='manager@manager.com', password='manager')

        pizza_json = self.create_pizza_json()

        # create new menu-item
        response = self.client.post(
            path = "/api/menu-items",
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get id of the created item
        id = response.data['id']
        id = id[id.rindex('/') + 1 : ]

        response = self.client.get(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 200)

        # post
        response = self.client.post(
            path = "/api/menu-items/{}".format(id),
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 405)

        # put
        response = self.client.put(
            path = "/api/menu-items/{}".format(id),
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

        # patch
        response = self.client.patch(
            path = "/api/menu-items/{}".format(id),
            data = pizza_json,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

        # to delete the item
        response = self.client.delete(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 204)

        # the item doesn't exist already, so we cannot delete it
        response = self.client.delete(path="/api/menu-items/{}".format(id), format="json")
        self.assertEqual(response.status_code, 404)
