from django.urls import path

from . import views



urlpatterns=[


path(
"trips/",
views.trip_list,
name="trip_list"
),


path(
"trip/add/",
views.trip_add,
name="trip_add"
),


path(
"trip/edit/<int:id>/",
views.trip_edit,
name="trip_edit"
),



path(
"fuel/",
views.fuel_list,
name="fuel_list"
),


path(
"fuel/add/",
views.fuel_add,
name="fuel_add"
),



path(
"expenses/",
views.expense_list,
name="expense_list"
),


path(
"expense/add/",
views.expense_add,
name="expense_add"
),


]