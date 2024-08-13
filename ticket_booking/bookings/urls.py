# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_ticket, name='book_ticket'),
    path('success/', views.booking_success, name='booking_success'),
]