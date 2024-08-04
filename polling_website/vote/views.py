# vote/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Candidate, Vote

def home(request):
    return render(request, 'vote/home.html')

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            messages.success(request, f'User {username} added successfully!')
        else:
            messages.error(request, 'Please enter a username!')
    return render(request, 'vote/add_user.html')

def polling_box(request):
    candidates = Candidate.objects.all()
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        if candidate_id:
            candidate = Candidate.objects.get(id=candidate_id)
            Vote.objects.create(candidate=candidate)
            messages.success(request, 'Your vote has been recorded!')
            return redirect('home')
        else:
            messages.error(request, 'Please select a candidate!')
    return render(request, 'vote/polling_box.html', {'candidates': candidates})

def results(request):
    candidates = Candidate.objects.all()
    results = []
    for candidate in candidates:
        vote_count = Vote.objects.filter(candidate=candidate).count()
        results.append({'candidate': candidate, 'votes': vote_count})
    return render(request, 'vote/results.html', {'results': results})