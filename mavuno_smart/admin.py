from django.contrib import admin
from .models import Farm, FarmData, FarmMapping, PaymentData, UserProfile, CarbonCredits, Verification, MarketListing, Transaction

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location', 'size')
    search_fields = ('name', 'location', 'user__username')
    ordering = ('name',)

@admin.register(FarmData)
class FarmDataAdmin(admin.ModelAdmin):
    list_display = ('farm', 'crop_type', 'area', 'yield_amount', 'date_planted', 'date_harvested', 'carbon_sequestered')
    search_fields = ('farm__name', 'crop_type', 'farm__user__username')
    list_filter = ('crop_type', 'date_planted', 'date_harvested')
    ordering = ('-date_planted',)

@admin.register(FarmMapping)
class FarmMappingAdmin(admin.ModelAdmin):
    list_display = ('farm', 'mapping_data')
    search_fields = ('farm__name', 'farm__user__username')
    ordering = ('farm',)

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

@admin.register(CarbonCredits)
class CarbonCreditsAdmin(admin.ModelAdmin):
    list_display = ('farm', 'amount', 'verified', 'date_verified')
    search_fields = ('farm__name', 'farm__user__username')
    list_filter = ('verified', 'date_verified')
    ordering = ('-date_verified',)

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('carbon_credits', 'verifier', 'date_verified')
    search_fields = ('carbon_credits__farm__name', 'verifier__username')
    list_filter = ('date_verified',)
    ordering = ('-date_verified',)

@admin.register(MarketListing)
class MarketListingAdmin(admin.ModelAdmin):
    list_display = ('carbon_credits', 'price_per_ton', 'date_listed', 'available')
    search_fields = ('carbon_credits__farm__name',)
    list_filter = ('available', 'date_listed')
    ordering = ('-date_listed',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'market_listing', 'amount_purchased', 'total_price', 'date_purchased', 'payment_confirmed')
    search_fields = ('buyer__username', 'market_listing__carbon_credits__farm__name')
    list_filter = ('payment_confirmed', 'date_purchased')
    ordering = ('-date_purchased',)
