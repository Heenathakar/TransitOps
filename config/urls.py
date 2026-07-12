from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('fleet/', include('fleet.urls')),
    path('operations/', include('operations.urls')),
    path('reports/', include('reports.urls')),
]