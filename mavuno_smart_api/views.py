# mavuno_smart_api/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from mavuno_smart.models import Farm, FarmData, PaymentData, UserProfile, FarmMapping
from .serializers import UserSerializer, RegisterSerializer, FarmSerializer, FarmDataSerializer, PaymentDataSerializer, UserProfileSerializer, FarmMappingSerializer

class AuthView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated ,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class FarmViewSet(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FarmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmDataViewSet(generics.ListCreateAPIView):
    queryset = FarmData.objects.all()
    serializer_class = FarmDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class FarmDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmData.objects.all()
    serializer_class = FarmDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentDataViewSet(generics.ListCreateAPIView):
    queryset = PaymentData.objects.all()
    serializer_class = PaymentDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentData.objects.all()
    serializer_class = PaymentDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonalDetailsView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class FarmMappingViewSet(generics.ListCreateAPIView):
    queryset = FarmMapping.objects.all()
    serializer_class = FarmMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class FarmMappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmMapping.objects.all()
    serializer_class = FarmMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
