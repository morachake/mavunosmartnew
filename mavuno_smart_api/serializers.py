# mavuno_smart_api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from mavuno_smart.models import FarmData, PaymentData, UserProfile, FarmMapping

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

class FarmDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmData
        fields = '__all__'

class PaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentData
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class FarmMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmMapping
        fields = '__all__'
