from rest_framework import serializers
from django.contrib.auth.models import User
from mavuno_smart.models import FarmData, PaymentData, UserProfile, FarmMapping, Farm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name', 'location', 'size']

class FarmDataSerializer(serializers.ModelSerializer):
    farm = FarmSerializer()

    class Meta:
        model = FarmData
        fields = ['farm', 'crop_type', 'area', 'yield_amount', 'date_planted', 'date_harvested', 'carbon_sequestered']

class PaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentData
        fields = ['payment_info']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'contact_number', 'address']

class FarmMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmMapping
        fields = ['mapping_data']
