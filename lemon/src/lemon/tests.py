from django.test import TestCase

from api.models import Category, Cuisine, Meal


class MenuImagePathTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(slug="main", title="Main")
        cuisine = Cuisine.objects.create(name="Italian")
        cls.meal = Meal.objects.create(
            name="Bruschetta",
            cuisine=cuisine,
            category=category,
            price="7.35",
            image="/img/menu_items/Bruschetta.jpg",
            image_text="Bruschetta",
        )

    def test_menu_uses_relative_static_image_path(self):
        response = self.client.get("/menu")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/static/img/menu_items/Bruschetta.jpg")

    def test_menu_item_uses_relative_static_image_path(self):
        response = self.client.get(f"/menu-item/{self.meal.pk}")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/static/img/menu_items/Bruschetta.jpg")
