# mavuno_smart/models.py

from django.db import models
from django.contrib.auth.models import User

class FarmData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.data[:50]}"


class PaymentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_info = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.payment_info[:50]}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.bio[:50]}"


class FarmMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mapping_data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.mapping_data[:50]}"
