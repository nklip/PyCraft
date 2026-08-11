from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Booking, Cart, Category, Cuisine, Meal, Order, OrderItem

User = get_user_model()

# Allows to display the name of category for Booking
class BookingSerializer(serializers.ModelSerializer):
    # Could add a hyperlink instead of int id
    id = serializers.HyperlinkedRelatedField(many=False, view_name='booking', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'last_name', 'guest_count', 'reservation_date', 'reservation_time', 'comments']

# Allows to display the name of category for Meal
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

# Allows to display the name of cuisine for Meal
class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name']

class MealSerializer(serializers.ModelSerializer):
    # Could add a hyperlink instead of int id
    id = serializers.HyperlinkedRelatedField(many=False, view_name='menu-item-view', read_only=True)
    category = CategorySerializer()
    cuisine = CuisineSerializer()

    class Meta:
        model = Meal
        fields = ['id', 'category', 'cuisine', 'name', 'price', 'desc', 'image', 'image_text']#'__all__'

    def create(self, validated_data):
        # find category object by name
        category_data = validated_data.pop('category')
        # find category object by name
        category = Category.objects.get(title = category_data['title'])
        # add category
        validated_data["category"] = category

        # find cuisine object by name
        cuisine_data = validated_data.pop('cuisine')
        # find cuisine object by name
        cuisine = Cuisine.objects.get(name = cuisine_data['name'])
        # add cuisine
        validated_data["cuisine"] = cuisine

        # create new meal object in DB
        meal = Meal.objects.create(**validated_data)
        return meal

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        # find cuisine object by name
        category = Category.objects.get(title = category_data['title'])

        cuisine_data = validated_data.pop('cuisine')
        # find cuisine object by name
        cuisine = Cuisine.objects.get(name = cuisine_data['name'])

        instance.name = validated_data.get('name', instance.name)
        instance.category = category
        instance.cuisine = cuisine
        instance.price = validated_data.get('price', instance.price)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.image = validated_data.get('image', instance.image)
        instance.image_text = validated_data.get('image_text', instance.image_text)
        instance.save()

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [User._meta.pk.name, User.USERNAME_FIELD, 'first_name', 'last_name', 'email', 'is_active']

class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    meal_id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['user_id', 'meal_id', 'count', 'unit_price', 'price']
        read_only_fields = ['price']

    def create(self, validated_data):
        # find count and unit_price
        count = validated_data.get('count')
        unit_price = validated_data.get('unit_price')

        # calculate price
        validated_data["price"] = count * unit_price

        # create new cart object in DB
        cart = Cart.objects.create(**validated_data)
        return cart

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedRelatedField(many=False, view_name='order-item-view', read_only=True)
    customer_id = serializers.IntegerField()
    delivery_id = serializers.IntegerField()
    status = serializers.CharField()

    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'delivery_id', 'status']

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    meal_id = serializers.IntegerField()
    count = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['order_id', 'meal_id', 'count', 'unit_price', 'price']
        read_only_fields = ['price']

    def create(self, validated_data):
        # find count and unit_price
        count = validated_data.get('count')
        unit_price = validated_data.get('unit_price')

        # calculate price
        validated_data["price"] = count * unit_price

        # create new cart object in DB
        cart = Cart.objects.create(**validated_data)
        return cart
