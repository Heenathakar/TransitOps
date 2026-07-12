from django.urls import path

from . import views



urlpatterns=[


path(
'vehicles/',
views.vehicle_list,
name="vehicle_list"
),


path(
'vehicle/add/',
views.vehicle_add,
name="vehicle_add"
),



path(
'drivers/',
views.driver_list,
name="driver_list"
),


path(
'driver/add/',
views.driver_add,
name="driver_add"
),



path(
'maintenance/',
views.maintenance_list,
name="maintenance_list"
),


path(
'maintenance/add/',
views.maintenance_add,
name="maintenance_add"
),


]