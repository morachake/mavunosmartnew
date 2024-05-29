from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone

class FarmData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farmdata')
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100, default="unknown")
    area = models.FloatField(default=0.0)  
    yield_amount = models.FloatField(default=0.0)  
    date_planted = models.DateField(default=timezone.now)  
    date_harvested = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.farm_name} - {self.user.username}"
class PaymentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_info = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.payment_info[:50]}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="")
    contact_number = models.CharField(max_length=15, blank=True, default="")
    address = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.user.username
    
class FarmMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mapping_data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.mapping_data[:50]}"
