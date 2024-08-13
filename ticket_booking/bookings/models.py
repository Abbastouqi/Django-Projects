# bookings/models.py

from django.db import models

class Ticket(models.Model):
    DESTINATION_CHOICES = [
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        ('Miami', 'Miami'),
    ]

    TIME_CHOICES = [
        ('09:00', '09:00 AM'),
        ('12:00', '12:00 PM'),
        ('15:00', '03:00 PM'),
        ('18:00', '06:00 PM'),
    ]

    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    departure_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    passenger_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.destination} at {self.departure_time}"