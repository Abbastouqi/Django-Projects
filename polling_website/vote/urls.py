# vote/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
    path('polling_box/', views.polling_box, name='polling_box'),
    path('results/', views.results, name='results'),
]
