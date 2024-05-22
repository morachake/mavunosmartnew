from django.contrib import admin
from .models import FarmData, PaymentData, UserProfile, FarmMapping

@admin.register(FarmData)
class FarmDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm_name', 'location', 'crop_type', 'area', 'yield_amount', 'date_planted', 'date_harvested')
    search_fields = ('farm_name', 'location', 'crop_type', 'user__username')
    list_filter = ('crop_type', 'date_planted', 'date_harvested')
    ordering = ('-date_planted',)

@admin.register(PaymentData)
class PaymentDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_info')
    search_fields = ('user__username',)
    ordering = ('user',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number', 'address')
    search_fields = ('user__username', 'contact_number', 'address')
    ordering = ('user',)

@admin.register(FarmMapping)
class FarmMappingAdmin(admin.ModelAdmin):
    list_display = ('user', 'mapping_data')
    search_fields = ('user__username',)
    ordering = ('user',)
