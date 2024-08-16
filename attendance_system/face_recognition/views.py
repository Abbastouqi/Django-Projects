from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student, Attendance
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def take_attendance(request):
    if request.method == 'POST':
        # Implement face recognition and attendance marking here
        pass
    return render(request, 'take_attendance.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date', '-period')
    return render(request, 'attendance_list.html', {'attendances': attendances})

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_student(request):
    if request.method == 'POST':
        # Implement student addition logic
        pass
    return render(request, 'add_student.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def search_attendance(request):
    if request.method == 'POST':
        # Implement multi-parameter search logic
        pass
    return render(request, 'search_attendance.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_attendance(request, attendance_id):
    if request.method == 'POST':
        # Implement attendance update logic
        pass
    return render(request, 'update_attendance.html')



def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')