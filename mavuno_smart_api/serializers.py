from rest_framework import serializers
from django.contrib.auth.models import User
from mavuno_smart.models import Farm, FarmData, PaymentData, UserProfile, FarmMapping

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
        fields = ['id','user','name','loaction','size']
        

class FarmDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmData
        fields = ['farm_name', 'location', 'crop_type', 'area', 'yield_amount', 'date_planted', 'date_harvested']    

class PaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentData
        fields = ['id','user','payment_amount']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user','bio', 'contact_number', 'adress']

class FarmMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmMapping
        fields = ['id','farm','mapping_data']
