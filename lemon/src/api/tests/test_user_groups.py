from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase

from rest_framework.test import APIClient

# Create your tests here.

class UserGroupsTestCase(TestCase):

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
        self.manager1 = User.objects.create_user(
            username='manager1@manager1.com',
            password='manager1'
        )
        self.manager2 = User.objects.create_user(
            username='manager2@manager2.com',
            password='manager2'
        )

        # assign users into groups
        self.delivery1.groups.add(self.delivery_group)
        self.delivery1.save()

        self.delivery2.groups.add(self.delivery_group)
        self.delivery2.save()

        self.manager1.groups.add(self.manager_group)
        self.manager1.save()

        self.manager2.groups.add(self.manager_group)
        self.manager2.save()

    def test_manager_management(self):
        # manager 1
        self.user = self.manager1
        self.client.login(username='manager1@manager1.com', password='manager1')

        # get all managers
        response = self.client.get(path="/api/groups/manager/users", format="json")
        self.assertEqual(response.status_code, 200)

        # before change - there are only 2 managers
        managers = response.data
        self.assertEqual(2, managers['count'])
        self.assertEqual('manager1@manager1.com', managers['results'][0]['username'])
        self.assertEqual('manager2@manager2.com', managers['results'][1]['username'])

        # promote a customer to manager position
        data = {
            "username" : "customer1@customer1.com"
        }
        # add a new manager
        response = self.client.post(
            path="/api/groups/manager/users",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get all managers
        response = self.client.get(path="/api/groups/manager/users", format="json")
        self.assertEqual(response.status_code, 200)

        # after change - there are 3 managers
        managers = response.data
        self.assertEqual(3, managers['count'])
        self.assertEqual('customer1@customer1.com', managers['results'][0]['username'])
        self.assertEqual('manager1@manager1.com', managers['results'][1]['username'])
        self.assertEqual('manager2@manager2.com', managers['results'][2]['username'])

        # login as delivery guy
        self.user = self.delivery1
        self.client.login(username='delivery1@delivery1.com', password='delivery1')

        # access denied
        id = managers['results'][0]['id']
        response = self.client.delete(path="/api/groups/manager/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 403)

        # login as manager
        self.user = self.manager1
        self.client.login(username='manager1@manager1.com', password='manager1')

        # user not found
        response = self.client.delete(path="/api/groups/manager/users/99999", format="json")
        self.assertEqual(response.status_code, 404)

        # user is not a manager
        id = self.delivery1.id
        response = self.client.delete(path="/api/groups/manager/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 404)

        # access allowed to delete manager
        id = managers['results'][0]['id']
        response = self.client.delete(path="/api/groups/manager/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 200)

    def test_delivery_management(self):
        # manager 1
        self.user = self.manager1
        self.client.login(username='manager1@manager1.com', password='manager1')

        # get all delivery crew
        response = self.client.get(path="/api/groups/delivery-crew/users", format="json")
        self.assertEqual(response.status_code, 200)

        managers = response.data
        self.assertEqual(2, managers['count'])
        self.assertEqual('delivery1@delivery1.com', managers['results'][0]['username'])
        self.assertEqual('delivery2@delivery2.com', managers['results'][1]['username'])

        # promote a customer to a delivery guy
        data = {
            "username" : "customer2@customer2.com"
        }
        # add a new delivery
        response = self.client.post(
            path="/api/groups/delivery-crew/users",
            data = data,
            format = "json",
            headers = {'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        # get all delivery guys
        response = self.client.get(path="/api/groups/delivery-crew/users", format="json")
        self.assertEqual(response.status_code, 200)

        # after change - there are 3 delivery guys
        managers = response.data
        self.assertEqual(3, managers['count'])
        self.assertEqual('customer2@customer2.com', managers['results'][0]['username'])
        self.assertEqual('delivery1@delivery1.com', managers['results'][1]['username'])
        self.assertEqual('delivery2@delivery2.com', managers['results'][2]['username'])

        # login as delivery guy
        self.user = self.delivery1
        self.client.login(username='delivery1@delivery1.com', password='delivery1')

        # access denied
        id = managers['results'][0]['id']
        response = self.client.delete(path="/api/groups/delivery-crew/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 403)

        # login as manager
        self.user = self.manager1
        self.client.login(username='manager1@manager1.com', password='manager1')

        # user not found
        response = self.client.delete(path="/api/groups/delivery-crew/users/99999", format="json")
        self.assertEqual(response.status_code, 404)

        # user is not a delivery guy
        id = self.manager1.id
        response = self.client.delete(path="/api/groups/delivery-crew/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 404)

        # access allowed to delete a delivery guy
        id = managers['results'][0]['id']
        response = self.client.delete(path="/api/groups/delivery-crew/users/{}".format(id), format="json")
        self.assertEqual(response.status_code, 200)