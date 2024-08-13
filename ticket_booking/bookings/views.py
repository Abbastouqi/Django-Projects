# bookings/views.py

from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketBookingForm

def home(request):
    return render(request, 'home.html')

def book_ticket(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = TicketBookingForm()
    return render(request, 'book_ticket.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')