# blog/urls.py

from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
]   

