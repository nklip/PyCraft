# urls.py in lemon app
from django.urls import path, include
from lemon.views import BookingFormView

from . import views

urlpatterns = [

    #-------------------------
    # HTML templates
    #-------------------------
    path("",                               views.index,                 name='index'),
    path("index",                          views.index,                 name='index'),
    path('about',                          views.about,                 name='about'),
    path('menu',                           views.menu,                  name='menu'),
    path('menu-item/<int:pk>',             views.menu_item,             name="menu-item"),
    path('booking',                        BookingFormView.as_view(),   name="booking"),
    path('bookings',                       views.bookings,              name='bookings'),

    path('__debug__', include('debug_toolbar.urls')),
]