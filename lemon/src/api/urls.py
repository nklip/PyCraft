# urls.py in lemon app
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from .views.bookings import BookingsView, BookingView
from .views.cart import CartsView
from .views.menu_items import MealView, MealsView
from .views.orders import OrdersView, OrderView
from .views.user_groups import ManagersView, ManagerView, DeliveryCrewView, DeliveryPersonView

urlpatterns = [
    #-------------------------
    # reused API
    #-------------------------
    # could be used to generate an authentication token for a user
    path("token/login",              obtain_auth_token),
    #-------------------------
    # API
    #-------------------------
    path("api/bookings",                             BookingsView.as_view(),       name="bookings"),
    path("api/bookings/<int:pk>",                    BookingView.as_view(),        name="booking"),

    path("api/cart/menu-items",                      CartsView.as_view()),

    path("api/menu-items",                           MealsView.as_view()),
    path("api/menu-items/<int:pk>",                  MealView.as_view(),           name='menu-item-view'),

    path("api/orders",                               OrdersView.as_view()),
    path("api/orders/<int:pk>",                      OrderView.as_view(),          name='order-item-view'),

    path("api/groups/manager/users",                 ManagersView.as_view()),
    path("api/groups/manager/users/<int:pk>",        ManagerView.as_view(),        name='manager-view'),
    path("api/groups/delivery-crew/users",           DeliveryCrewView.as_view()),
    path("api/groups/delivery-crew/users/<int:pk>",  DeliveryPersonView.as_view(), name='delivery-person-view'),

]