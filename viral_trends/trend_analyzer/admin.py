from django.contrib import admin
from .models import Platform, Trend, BusinessProfile, AdSuggestion

# Register your models here
admin.site.register(Platform)
admin.site.register(Trend)
admin.site.register(BusinessProfile)
admin.site.register(AdSuggestion)