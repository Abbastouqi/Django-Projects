from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Trend, BusinessProfile, AdSuggestion
from .trend_fetcher import fetch_google_trends

@login_required
def dashboard(request):
    business, created = BusinessProfile.objects.get_or_create(user=request.user)
    
    # Get search query
    query = request.GET.get('q')
    
    if query:
        # Fetch new trend data from Google Trends
        fetch_google_trends(query)
        
        # Filter trends based on search query
        trends = Trend.objects.filter(
            Q(keyword__icontains=query) | 
            Q(platform__name__icontains=query)
        ).order_by('-timestamp')[:10]
    else:
        trends = Trend.objects.order_by('-timestamp')[:10]
    
    ad_suggestions = AdSuggestion.objects.filter(business=business).order_by('-created_at')[:5]
    
    return render(request, 'dashboard.html', {
        'business': business,
        'trends': trends,
        'ad_suggestions': ad_suggestions,
        'query': query,
    })

def trend_list(request):
    trends = Trend.objects.order_by('-timestamp')[:50]
    return render(request, 'trend_list.html', {'trends': trends})