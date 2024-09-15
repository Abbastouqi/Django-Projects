from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Trend(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    volume = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=50)

class AdSuggestion(models.Model):
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    trend = models.ForeignKey(Trend, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

