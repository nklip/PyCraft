from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

from api.tests.test_cart import create_pizza, create_margarita, add_meal_item_in_cart

# Create your tests here.

class OrdersTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # create groups
        self.delivery_group = Group(name = "DeliveryCrew")
        self.delivery_group.save()

        self.manager_group = Group(name = "Manager")
        self.manager_group.save()

        # create users
        self.customer1 = User.objects.create_user(
            username='customer1@customer1.com',
            password='customer1'
        )
        self.customer2 = User.objects.create_user(
            username='customer2@customer2.com',
            password='customer2'
        )
        self.delivery1 = User.objects.create_user(
            username='delivery1@delivery1.com',
            password='delivery1'
        )
        self.delivery2 = User.objects.create_user(
            username='delivery2@delivery2.com',
            password='delivery2'
        )
        self.manager = User.objects.create_user(
            username='manager@manager.com',
            password='manager'
        )

        # assign users into groups
        self.delivery1.groups.add(self.delivery_group)
        self.delivery1.save()

        self.delivery2.groups.add(self.delivery_group)
        self.delivery2.save()

        self.manager.groups.add(self.manager_group)
        self.manager.save()

    def test_customers_visibility(self):
        # Customer 1
        self.user = self.customer1
        self.client.login(username='customer1@customer1.com', password='customer1')

        response = self.client.get(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 200)

        # Order is empty
        orders = response.data
        self.assertEqual(0, orders['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 1, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 1, margarita)
        self.assertEqual(response.status_code, 201)

        # create Order for Customer 1
        response = self.client.post(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])

        # Customer 2
        self.user = self.customer2
        self.client.login(username='customer2@customer2.com', password='customer2')

        # We don't see orders for Customer1
        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(0, orders['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 2, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 2, margarita)
        self.assertEqual(response.status_code, 201)

        # create Order for Customer 2
        response = self.client.post(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])

        # Manager
        self.user = self.manager
        self.client.login(username='manager@manager.com', password='manager')

        # we can see both Orders from different customers
        response = self.client.get(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 200)
        orders = response.data
        self.assertEqual(2, orders['count'])

    def test_delivery_lifecycle(self):
        # Customer 1
        self.user = self.customer1
        self.client.login(username='customer1@customer1.com', password='customer1')

        response = self.client.get(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 200)

        # Order is empty
        orders = response.data
        self.assertEqual(0, orders['count'])

        # add pizza in Cart
        pizza = create_pizza()
        response = add_meal_item_in_cart(self.user, self.client, 1, pizza)
        self.assertEqual(response.status_code, 201)

        # add margarita in Cart
        margarita = create_margarita()
        response = add_meal_item_in_cart(self.user, self.client, 1, margarita)
        self.assertEqual(response.status_code, 201)

        # create Order for Customer 1
        response = self.client.post(path="/api/orders", format="json")
        self.assertEqual(response.status_code, 201)

        # get order id
        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])
        # get full id
        order_id = orders['results'][0]['id']
        # get number id
        order_id = order_id[order_id.rindex('/') + 1 : ]

        # login as customer2
        self.user = self.customer2
        self.client.login(username='customer2@customer2.com', password='customer2')

        # no orders for customer2
        response = self.client.get(path="/api/orders/{}".format(order_id), format="json")
        self.assertEqual(response.status_code, 403)
        self.assertEqual('Access denied.', response.data)

        # login as DeliveryCrew
        self.user = self.delivery1
        self.client.login(username='delivery1@delivery1.com', password='delivery1')

        # check assigned deliveries for DeliveryCrew
        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(0, orders['count'])

        # login as Manager
        self.user = self.manager
        self.client.login(username='manager@manager.com', password='manager')

        order_change = {
            "delivery_id" : self.delivery1.id
        }

        response = self.client.patch(
            path = "/api/orders/{}".format(order_id),
            data = order_change,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, orders['count'])

        # login as DeliveryCrew
        self.user = self.delivery1
        self.client.login(username='delivery1@delivery1.com', password='delivery1')

        # check assigned deliveries for DeliveryCrew
        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])

        # update status as DeliveryCrew to delivered
        order_change = {
            "status" : True
        }

        response = self.client.patch(
            path = "/api/orders/{}".format(order_id),
            data = order_change,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )

        response = self.client.get(path="/api/orders", format="json")
        orders = response.data
        self.assertEqual(1, orders['count'])
        self.assertEqual('True', orders['results'][0]['status'])

        # try to delete order as delivery crew
        response = self.client.delete(
            path = "/api/orders/{}".format(order_id),
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 403)

        # login as Manager
        self.user = self.manager
        self.client.login(username='manager@manager.com', password='manager')

        # delete order
        response = self.client.delete(
            path = "/api/orders/{}".format(order_id),
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual('Order has been deleted.', response.data)

