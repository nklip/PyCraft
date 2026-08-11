from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# API models

TIME_SLOTS = {
    "1 PM": "1 PM",
    "2 PM": "2 PM",
    "3 PM": "3 PM",
    "4 PM": "4 PM",
    "5 PM": "5 PM",
    "6 PM": "6 PM",
    "7 PM": "7 PM",
    "8 PM": "8 PM",
    "9 PM": "9 PM",
}

class Booking(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    guest_count = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(10)])
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=10, choices=TIME_SLOTS)
    comments = models.CharField(max_length = 100)

    # also show it in admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date} - {self.reservation_time}"

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 255, db_index = True)

    # also show it in admin panel
    def __str__(self):
        return f"{self.title}"

class Cuisine(models.Model):
    name = models.CharField(max_length = 100)

    # also show it in admin panel
    def __str__(self):
        return f"{self.name}"

class Meal(models.Model):
    name = models.CharField(max_length = 100, db_index=True)
    cuisine  = models.ForeignKey(Cuisine,  on_delete = models.PROTECT)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    price    = models.DecimalField(max_digits = 5, decimal_places = 2)
    desc       = models.TextField(max_length = 1000, default = '')
    image      = models.CharField(max_length = 200, default = '')
    image_text = models.CharField(max_length = 200, default = '')

    @property
    def static_image_path(self):
        return self.image.lstrip('/')

    # also show it in admin panel
    def __str__(self):
        return f"{self.name} - {self.price}"

class Cart(models.Model):
    user  = models.ForeignKey(User, on_delete = models.PROTECT)
    meal  = models.ForeignKey(Meal, on_delete = models.PROTECT)
    count = models.IntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    price      = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        unique_together = ('user', 'meal')

    # also show it in admin panel
    def __str__(self):
        return f"{self.user} - {self.meal} - {self.count}"

class Order(models.Model):
    customer = models.ForeignKey(User, related_name = 'customer', on_delete = models.PROTECT)
    delivery = models.ForeignKey(User, related_name = 'delivery', on_delete = models.PROTECT, null = True)
    status = models.BooleanField(db_index = True, default = 0, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    date = models.DateField(db_index = True)

    # also show it in admin panel
    def __str__(self):
        st_text = ""
        if self.delivery != None and self.status == False:
            st_text = "Out for delivery"
        elif not self.delivery and self.status == False:
            st_text = "Not assigned"
        else:
            st_text = "Delivered"
        return f"Order '{self.id}' for '{self.customer}' has status '{st_text}'. Assigned to '{self.delivery}'"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    meal  = models.ForeignKey(Meal,  on_delete = models.PROTECT)
    count = models.IntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    price      = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        unique_together = ('order', 'meal')

    # also show it in admin panel
    def __str__(self):
        return f"{self.order} - {self.meal} - {self.count}"
