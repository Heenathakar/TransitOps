from django.urls import path
from . import views

urlpatterns = [

    # ── Vehicles ──────────────────────────────────────────
    path('vehicles/',               views.vehicle_list,   name='vehicle_list'),
    path('vehicle/add/',            views.vehicle_add,    name='vehicle_add'),
    path('vehicle/edit/<int:pk>/',  views.vehicle_edit,   name='vehicle_edit'),
    path('vehicle/delete/<int:pk>/', views.vehicle_delete, name='vehicle_delete'),

    # ── Drivers ───────────────────────────────────────────
    path('drivers/',                views.driver_list,    name='driver_list'),
    path('driver/add/',             views.driver_add,     name='driver_add'),
    path('driver/edit/<int:pk>/',   views.driver_edit,    name='driver_edit'),
    path('driver/delete/<int:pk>/', views.driver_delete,  name='driver_delete'),

    # ── Maintenance ───────────────────────────────────────
    path('maintenance/',                    views.maintenance_list,   name='maintenance_list'),
    path('maintenance/add/',                views.maintenance_add,    name='maintenance_add'),
    path('maintenance/delete/<int:pk>/',    views.maintenance_delete, name='maintenance_delete'),
]