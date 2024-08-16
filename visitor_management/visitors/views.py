from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.utils import timezone
from datetime import timedelta
from .models import Visitor
from .forms import VisitorForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages







def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')

from django.db.models import F
from django.db.models.functions import TruncDate

@login_required
def dashboard(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    last_7_days = today - timedelta(days=7)

    total_count = Visitor.objects.count()
    today_count = Visitor.objects.filter(date__date=today).count()
    yesterday_count = Visitor.objects.filter(date__date=yesterday).count()
    last_7_days_count = Visitor.objects.filter(date__date__gte=last_7_days).count()
    
    # Calculate 'Others' count
    others_count = total_count - today_count - yesterday_count - last_7_days_count

    context = {
        'today_count': today_count,
        'yesterday_count': yesterday_count,
        'last_7_days_count': last_7_days_count,
        'total_count': total_count,
        'others_count': others_count,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.created_by = request.user
            visitor.save()
            return redirect('dashboard')
    else:
        form = VisitorForm()
    return render(request, 'add_visitor.html', {'form': form})

@login_required
def manage_visitors(request):
    visitors = Visitor.objects.filter(created_by=request.user)
    return render(request, 'manage_visitors.html', {'visitors': visitors})

@login_required
def edit_visitor(request, visitor_id):
    visitor = Visitor.objects.get(id=visitor_id, created_by=request.user)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('manage_visitors')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'edit_visitor.html', {'form': form, 'visitor': visitor})