from django.shortcuts import render
from django.http import HttpResponse
import csv

from fleet.models import Vehicle, Driver, Maintenance

try:
    from operations.models import Trip, FuelLog, Expense
except:
    Trip = None
    FuelLog = None
    Expense = None


def dashboard(request):

    context = {
        "vehicle_count": Vehicle.objects.count(),
        "driver_count": Driver.objects.count(),
        "maintenance_count": Maintenance.objects.count(),
        "trip_count": Trip.objects.count() if Trip else 0,
        "fuel_count": FuelLog.objects.count() if FuelLog else 0,
        "expense_count": Expense.objects.count() if Expense else 0,
    }

    return render(request, "reports/dashboard.html", context)


def analytics(request):

    context = {
        "vehicles": Vehicle.objects.all(),
        "drivers": Driver.objects.all(),
        "maintenances": Maintenance.objects.all(),
        "trips": Trip.objects.all() if Trip else [],
        "fuels": FuelLog.objects.all() if FuelLog else [],
        "expenses": Expense.objects.all() if Expense else [],
    }

    return render(request, "reports/analytics.html", context)


def charts(request):

    context = {
        "vehicle_count": Vehicle.objects.count(),
        "driver_count": Driver.objects.count(),
        "maintenance_count": Maintenance.objects.count(),
        "trip_count": Trip.objects.count() if Trip else 0,
    }

    return render(request, "reports/charts.html", context)


def export_csv(request):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="vehicles.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Vehicle Number",
        "Model",
        "Capacity"
    ])

    for vehicle in Vehicle.objects.all():
        writer.writerow([
            vehicle.vehicle_number,
            vehicle.model,
            vehicle.capacity
        ])

    return response