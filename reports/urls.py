from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='reports_dashboard'   # renamed to avoid conflict with accounts 'dashboard'
    ),

    path(
        'analytics/',
        views.analytics,
        name='analytics'
    ),

    path(
        'charts/',
        views.charts,
        name='charts'
    ),

    path(
        'export/csv/',
        views.export_csv,
        name='export_csv'
    ),
]