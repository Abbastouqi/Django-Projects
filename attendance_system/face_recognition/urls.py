from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('take-attendance/', views.take_attendance, name='take_attendance'),
    path('attendance-list/', views.attendance_list, name='attendance_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('search-attendance/', views.search_attendance, name='search_attendance'),
    path('update-attendance/<int:attendance_id>/', views.update_attendance, name='update_attendance'),
]