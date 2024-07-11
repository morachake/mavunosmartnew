from django.urls import path
from . import views

app_name = 'mavuno_smart'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/charts/', views.charts_view, name='charts'),
    path('dashboard/tables/', views.tables_view, name='tables'),
]
