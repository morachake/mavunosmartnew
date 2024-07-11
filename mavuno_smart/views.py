from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')
def dashboard_view(request):
    return render(request, 'base.html')

def charts_view(request):
    return render(request, 'charts.html')

def tables_view(request):
    return render(request, 'tables.html')
