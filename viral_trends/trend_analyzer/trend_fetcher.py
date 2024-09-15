from pytrends.request import TrendReq
from .models import Platform, Trend
from django.utils import timezone

def fetch_google_trends(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], timeframe='now 1-d')
    
    interest_over_time_df = pytrends.interest_over_time()
    
    if not interest_over_time_df.empty:
        # Get the latest trend value
        latest_trend = interest_over_time_df[keyword].iloc[-1]
        
        # Get or create the Google platform
        platform, _ = Platform.objects.get_or_create(name='Google')
        
        # Create a new trend
        Trend.objects.create(
            platform=platform,
            keyword=keyword,
            volume=latest_trend,
            timestamp=timezone.now()
        )
        
        return latest_trend
    else:
        return None