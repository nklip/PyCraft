from django import forms

from django.utils import timezone

# import model from API
from api.models import Booking

class BookingForm(forms.ModelForm):
    # set initial values
    reservation_date = forms.DateField(initial = timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        model = Booking
        fields = '__all__'

