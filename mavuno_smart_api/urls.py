from django.urls import path
from .views import AuthView, RegisterView, LogoutView, FarmViewSet, FarmDetailView, FarmDataViewSet, FarmDataDetailView, PaymentDataViewSet, PaymentDataDetailView, PersonalDetailsView, FarmMappingViewSet, FarmMappingDetailView

app_name = 'mavuno_smart_api'

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('farms/', FarmViewSet.as_view(), name='farm_list_create'),
    path('farms/<int:pk>/', FarmDetailView.as_view(), name='farm_detail'),
    path('farm-data/', FarmDataViewSet.as_view(), name='farm_data_list_create'),
    path('farm-data/<int:pk>/', FarmDataDetailView.as_view(), name='farm_data_detail'),
    path('payment-data/', PaymentDataViewSet.as_view(), name='payment_data_list_create'),
    path('payment-data/<int:pk>/', PaymentDataDetailView.as_view(), name='payment_data_detail'),
    path('personal-details/', PersonalDetailsView.as_view(), name='personal_details'),
    path('farm-mapping/', FarmMappingViewSet.as_view(), name='farm_mapping_list_create'),
    path('farm-mapping/<int:pk>/', FarmMappingDetailView.as_view(), name='farm_mapping_detail'),
]
