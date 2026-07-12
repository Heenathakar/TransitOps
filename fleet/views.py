from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Vehicle, Driver, Maintenance
from .forms import VehicleForm, DriverForm, MaintenanceForm


# ════════════════════════════════════════════
# VEHICLE
# ════════════════════════════════════════════

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('vehicle_number')
    return render(request, 'fleet/vehicle_list.html', {'vehicles': vehicles})


@login_required
def vehicle_add(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Vehicle added successfully.')
        return redirect('vehicle_list')
    return render(request, 'fleet/vehicle_add.html', {'form': form})


@login_required
def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        messages.success(request, f'Vehicle {vehicle.vehicle_number} updated successfully.')
        return redirect('vehicle_list')
    return render(request, 'fleet/vehicle_edit.html', {'form': form, 'vehicle': vehicle})


@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        number = vehicle.vehicle_number
        vehicle.delete()
        messages.success(request, f'Vehicle {number} deleted.')
        return redirect('vehicle_list')
    return render(request, 'fleet/vehicle_list.html', {'vehicles': Vehicle.objects.all()})


# ════════════════════════════════════════════
# DRIVER
# ════════════════════════════════════════════

@login_required
def driver_list(request):
    drivers = Driver.objects.all().order_by('name')
    return render(request, 'fleet/driver_list.html', {'drivers': drivers})


@login_required
def driver_add(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Driver registered successfully.')
        return redirect('driver_list')
    return render(request, 'fleet/driver_add.html', {'form': form})


@login_required
def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    form = DriverForm(request.POST or None, instance=driver)
    if form.is_valid():
        form.save()
        messages.success(request, f'Driver {driver.name} updated successfully.')
        return redirect('driver_list')
    return render(request, 'fleet/driver_edit.html', {'form': form, 'driver': driver})


@login_required
def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        name = driver.name
        driver.delete()
        messages.success(request, f'Driver {name} deleted.')
        return redirect('driver_list')
    return redirect('driver_list')


# ════════════════════════════════════════════
# MAINTENANCE
# ════════════════════════════════════════════

@login_required
def maintenance_list(request):
    data = Maintenance.objects.all().order_by('-date')
    return render(request, 'fleet/maintenance_list.html', {'data': data})


@login_required
def maintenance_add(request):
    form = MaintenanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Maintenance record added successfully.')
        return redirect('maintenance_list')
    return render(request, 'fleet/maintenance_add.html', {'form': form})


@login_required
def maintenance_delete(request, pk):
    record = get_object_or_404(Maintenance, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Maintenance record deleted.')
        return redirect('maintenance_list')
    return redirect('maintenance_list')