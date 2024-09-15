from collections import Counter
from .models import Trend, Platform

def analyze_trends(trends_data):
    all_trends = []
    for platform, trends in trends_data.items():
        platform_obj, _ = Platform.objects.get_or_create(name=platform)
        for trend in trends:
            all_trends.append(trend['name'])
            Trend.objects.create(
                platform=platform_obj,
                keyword=trend['name'],
                volume=trend.get('tweet_volume', 0)
            )
    
    # Analyze overall trends
    trend_counter = Counter(all_trends)
    top_trends = trend_counter.most_common(10)
    return top_trends