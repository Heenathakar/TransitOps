from django.urls import path
from . import views

urlpatterns = [

    # ── Trips ─────────────────────────────────────────────
    path('trips/',                  views.trip_list,    name='trip_list'),
    path('trip/add/',               views.trip_add,     name='trip_add'),
    path('trip/edit/<int:pk>/',     views.trip_edit,    name='trip_edit'),
    path('trip/delete/<int:pk>/',   views.trip_delete,  name='trip_delete'),

    # ── Fuel Logs ─────────────────────────────────────────
    path('fuel/',                   views.fuel_list,    name='fuel_list'),
    path('fuel/add/',               views.fuel_add,     name='fuel_add'),
    path('fuel/delete/<int:pk>/',   views.fuel_delete,  name='fuel_delete'),

    # ── Expenses ──────────────────────────────────────────
    path('expenses/',               views.expense_list,   name='expense_list'),
    path('expense/add/',            views.expense_add,    name='expense_add'),
    path('expense/delete/<int:pk>/', views.expense_delete, name='expense_delete'),
]