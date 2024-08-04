# vote/models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.symbol}"

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name}"