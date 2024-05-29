from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.FloatField(help_text="Size of the farm in acres")

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class FarmData(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_data', null=True, blank=True)
    crop_type = models.CharField(max_length=100, default="unknown")
    area = models.FloatField(default=0.0)
    yield_amount = models.FloatField(default=0.0)
    date_planted = models.DateField(default=timezone.now)
    date_harvested = models.DateField(null=True, blank=True)
    carbon_sequestered = models.FloatField(help_text="Carbon sequestered in tons", default=0.0)

    def __str__(self):
        return f"{self.farm.name} - {self.crop_type}" if self.farm else f"No Farm - {self.crop_type}"

class FarmMapping(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, blank=True)
    mapping_data = models.TextField()

    def __str__(self):
        return f"{self.farm.name} - {self.mapping_data[:50]}" if self.farm else f"No Farm - {self.mapping_data[:50]}"

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

class CarbonCredits(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='carbon_credits')
    amount = models.FloatField(help_text="Amount of carbon credits in tons")
    verified = models.BooleanField(default=False)
    date_verified = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.farm.name} - {self.amount} tons"

class Verification(models.Model):
    carbon_credits = models.OneToOneField(CarbonCredits, on_delete=models.CASCADE, related_name='verification')
    verifier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verifications')
    date_verified = models.DateField(auto_now_add=True)
    verification_report = models.TextField()

    def __str__(self):
        return f"{self.carbon_credits.farm.name} Verification"

class MarketListing(models.Model):
    carbon_credits = models.OneToOneField(CarbonCredits, on_delete=models.CASCADE, related_name='market_listing')
    price_per_ton = models.DecimalField(max_digits=10, decimal_places=2)
    date_listed = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.carbon_credits.farm.name} Listing"

class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    market_listing = models.ForeignKey(MarketListing, on_delete=models.CASCADE, related_name='transactions')
    amount_purchased = models.FloatField(help_text="Amount of carbon credits purchased in tons")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateField(auto_now_add=True)
    payment_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyer.username} - {self.market_listing.carbon_credits.farm.name}"
