
# api/user_groups.py in lemon app
import json

from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from rest_framework import status, serializers, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from ..models import Cart, Order, OrderItem
from ..serializers import OrderSerializer

def access_denied():
    return HttpResponseForbidden("Access denied. You are not a manager")

#-------------------------
# API:
#
# /api/orders           - Customer      - GET   - Returns all orders with order items created by this user
# /api/orders           - Customer      - POST  - Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.
# /api/orders/{orderId} - Customer      - GET   - Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.
# /api/orders/{orderId} - Manager       - PUT, PATCH -
# Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.
# If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery.
# If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered.
# /api/orders           - Manager       - GET    - Returns all orders with order items by all users
# /api/orders/{orderId} - Manager       - DELETE - Deletes this order
# /api/orders           - Delivery crew - GET    - Returns all orders with order items assigned to the delivery crew
# /api/orders/{orderId} - Delivery crew - PATCH  - A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.
#-------------------------

@permission_classes([IsAuthenticated])
class OrdersView(generics.CreateAPIView, generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post']
    queryset = Order.objects.get_queryset()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    # override for get & post
    def get_queryset(self):
        user = self.request.user
        if (self.request.user.groups.filter(name='Manager')).exists():
            return Order.objects.all().order_by('id')
        elif (self.request.user.groups.filter(name='DeliveryCrew').exists()):
            return Order.objects.all().filter(delivery=user).order_by('id')
        else:
            return Order.objects.all().filter(customer=user).order_by('id')

    def post(self, request, *args, **kwargs):
        # get user id
        user = self.request.user
        # get all cart items
        cart_items = Cart.objects.all().filter(user=user)

        if not cart_items.exists():
            return Response("Your cart is empty.", status=status.HTTP_200_OK)

        # find final price
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.price

        # get current time
        date = timezone.now().strftime("%Y-%m-%d")
        # create a new order
        order = Order(customer=user, price=total_price, date=date)
        order.save()

        # create order items from cart items
        for cart_item in cart_items:
            order_item = OrderItem(
                order = order,
                meal = cart_item.meal,
                count = cart_item.count,
                unit_price = cart_item.unit_price,
                price =cart_item.price
            )
            order_item.save()

        # clear cart items
        for cart_item in cart_items:
            cart_item.delete()

        return Response("Your order has been created.", status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class OrderView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = Order.objects.values()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def update(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='DeliveryCrew')).exists():
            # get order
            order = Order.objects.all().filter(pk=kwargs.get('pk'))
            # delivery crew can only update status to delivered (1)
            st = request.data.get('status')
            if st == 'true' or st == 'True' or st == 1:
                order.update(status='True')

            return Response("Order has been updated.", status=status.HTTP_200_OK)
        elif (request.user.groups.filter(name='Manager')).exists():
            # get order
            order = Order.objects.all().filter(pk=kwargs.get('pk'))
            # update delivery
            delivery = request.data.get('delivery_id')
            if delivery:
                order.update(delivery=delivery)

            # Manager can only update status to assigned(0) or delivered (1)
            st = request.data.get('status')
            if st == 'true' or st == 'True' or st == 1:
                order.update(status='True')

            return Response("Order has been updated.", status=status.HTTP_200_OK)
        else:
            return access_denied()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # get order
        order = Order.objects.all().filter(pk=kwargs.get('pk')).first()
        # check if delivery guy is assigned
        delivery = 0
        if order.delivery:
            if order.delivery.pk:
                delivery = order.delivery.pk
        # check if order belongs the the user and if user is not a manager or not a delivery guy who has been assigned with this order
        if order.customer.pk != request.user.id and not delivery == request.user.id and not request.user.groups.filter(name='Manager').exists():
            return Response("Access denied.", status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            # get order
            order = Order.objects.all().filter(pk=kwargs.get('pk'))
            # get all order items for this order
            order_items = OrderItem.objects.all().filter(order=order.first())
            # delete all order items
            for order_item in order_items:
                order_item.delete()
            # delete order
            order.delete()

            return Response("Order has been deleted.", status=status.HTTP_204_NO_CONTENT)
        else:
            return access_denied()
