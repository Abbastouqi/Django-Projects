from .models import Trend, BusinessProfile, AdSuggestion

def generate_ad_suggestions(business):
    trends = Trend.objects.order_by('-volume')[:10]
    for trend in trends:
        suggestion = f"Incorporate '{trend.keyword}' into your next {business.business_type} promotion. Create a {business.business_type}-themed post using #{trend.keyword}."
        AdSuggestion.objects.create(
            business=business,
            trend=trend,
            suggestion=suggestion
        )