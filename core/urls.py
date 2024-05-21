from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mavuno_smart_api.urls', namespace='mavuno_smart_api')),
    path('', include('mavuno_smart.urls', namespace='mavuno_smart')),
]
