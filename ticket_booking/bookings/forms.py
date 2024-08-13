# bookings/forms.py

from django import forms
from .models import Ticket

class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['destination', 'departure_time', 'passenger_name']