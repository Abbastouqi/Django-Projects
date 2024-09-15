from celery import shared_task
from .social_media_integration import get_twitter_trends, get_facebook_trends, get_google_trends
from .trend_analysis import analyze_trends
from .ad_suggestions import generate_ad_suggestions
from .models import BusinessProfile

@shared_task
def fetch_and_analyze_trends():
    trends_data = {
        'twitter': get_twitter_trends(),
        'facebook': get_facebook_trends(),
        'google': get_google_trends(),
    }
    analyze_trends(trends_data)

@shared_task
def generate_suggestions_for_businesses():
    businesses = BusinessProfile.objects.all()
    for business in businesses:
        generate_ad_suggestions(business)