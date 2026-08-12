from django import forms
from django.utils import timezone

# import model from API
from api.models import Booking


class BookingForm(forms.ModelForm):
    # set initial values
    reservation_date = forms.DateField(initial=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        model = Booking
        # Listed explicitly so a new model field is never exposed by accident.
        fields = [
            "first_name",
            "last_name",
            "guest_count",
            "reservation_date",
            "reservation_time",
            "comments",
        ]
