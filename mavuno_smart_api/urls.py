# mavuno_smart_api/urls.py

from django.urls import path
from .views import AuthView, RegisterView, LogoutView, AddFarmDataView, PaymentDataView, PersonalDetailsView, FarmMappingView

app_name = 'mavuno_smart_api'

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-farm-data/', AddFarmDataView.as_view(), name='add_farm_data'),
    path('payment-data/', PaymentDataView.as_view(), name='payment_data'),
    path('personal-details/', PersonalDetailsView.as_view(), name='personal_details'),
    path('farm-mapping/', FarmMappingView.as_view(), name='farm_mapping'),
]
