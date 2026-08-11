# views.py in lemon app
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from datetime import timedelta

from lemon.forms import BookingForm

# import model from API
from api.models import Meal, Booking, TIME_SLOTS

# we provide up to 2 guests per day for booking
TOTAL_AVAILABLE_PLACES = 2

# Class-based view
class BookingFormView(View):
    def get(self, request):
        print("GET from BookingView...")

        booking = BookingForm()
        return self.render_new_booking(request, booking)

    def post(self, request):
        print("POST from BookingView...")

        booking = BookingForm(request.POST)
        if booking.is_valid:
            # do business validation
            first_name = booking.data.get('first_name')
            last_name = booking.data.get('last_name')
            reservation_date = booking.data.get('reservation_date')
            reservation_time = booking.data.get('reservation_time')
            guest_count = int(booking.data.get('guest_count'))

            print(reservation_date, reservation_time)

            booking_items = Booking.objects.all().filter(
                reservation_date=reservation_date,
                reservation_time=reservation_time
            )

            all_guests_count = guest_count
            for item in booking_items:
                all_guests_count += item.guest_count

            if all_guests_count > TOTAL_AVAILABLE_PLACES:
                return JsonResponse({
                    'message': 'Fail - Dear {first} {last}, unfortunately we do not have enough space capacity on {date} at {time} for {guests} people! Please try to choose another date and time!'
                    .format(first=first_name, last=last_name, date=reservation_date, time=reservation_time, guests=guest_count)
                })

            booking.save()
            # javascript reset the form on the 'Success' in the beginning of the message

            return JsonResponse({
                'message': 'Success - Booking for {first_name} {last_name} completed!'.format(first_name=first_name, last_name=last_name)
            })
        return self.render_new_booking(request, booking)

    @classmethod
    def render_new_booking(self, request, booking):
        # create default time_slots
        time_slots = {}
        for key in TIME_SLOTS.keys():
            time_slots[key] = "enabled"
        # Little Lemon doesn't provide booking more than for a week
        start_date = timezone.now()
        end_date = start_date + timedelta(days=7)

        # default date
        reservation_date = start_date.strftime("%Y-%m-%d")
        # get date from url variable
        if request.GET.get('date'):
            reservation_date = request.GET.get('date')
        booking_items = Booking.objects.all().filter(reservation_date=reservation_date)

        # check that we have space - no more than 2 people per hour
        for time_slot in time_slots.keys():
            total_guests = 0;
            booking_items_for_time_slot = booking_items.filter(reservation_time=time_slot)

            for item in booking_items_for_time_slot:
                total_guests += item.guest_count

            if total_guests >= TOTAL_AVAILABLE_PLACES:
                time_slots[time_slot] = "disabled"
        # find default amount of places for booking
        default_guests = 2
        min_guests = 1

        # create context for template
        context = {
            "form": booking,
            "reservation_date": reservation_date,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "default_guests": default_guests,
            "min_guests" : min_guests,
            "max_guests" : TOTAL_AVAILABLE_PLACES,
            "time_slots": time_slots,
        }
        return render(request, "booking.html", context)

def bookings(request):
    # show bookings between today and a week in advance
    start_date = timezone.now()
    end_date = start_date + timedelta(days=7)
    booking_items = Booking.objects.all().filter(
        reservation_date__gte=start_date.strftime("%Y-%m-%d"),
        reservation_date__lte=end_date.strftime("%Y-%m-%d")
    ).order_by('reservation_date', 'reservation_time')
    items_dict = {"bookings": booking_items}
    return render(request, "bookings.html", items_dict)

def index(request):
    return render(request, "index.html")

def menu(request):
    meal_items = Meal.objects.all()
    items_dict = { "menu": meal_items }
    return render(request, "menu.html", items_dict)

def menu_item(request, pk):
    try:
        item = Meal.objects.get(pk=pk);
    except Meal.DoesNotExist:
        print("Meal object doesn't exist for pk = {}".format(pk))
        item = ""
    item_dict = {"item": item }
    return render(request, "menu_item.html", item_dict)


def about(request):
    return render(request, "about.html")