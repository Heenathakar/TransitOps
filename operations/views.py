from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Trip, FuelLog, Expense
from .forms import TripForm, FuelForm, ExpenseForm


# ════════════════════════════════════════════
# TRIP
# ════════════════════════════════════════════

@login_required
def trip_list(request):
    trips = Trip.objects.all().select_related('vehicle', 'driver').order_by('-start_date')
    return render(request, 'operations/trip_list.html', {'trips': trips})


@login_required
def trip_add(request):
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Trip created successfully.')
        return redirect('trip_list')
    return render(request, 'operations/trip_add.html', {'form': form})


@login_required
def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    form = TripForm(request.POST or None, instance=trip)
    if form.is_valid():
        form.save()
        messages.success(request, f'Trip {trip.trip_number} updated successfully.')
        return redirect('trip_list')
    return render(request, 'operations/trip_edit.html', {'form': form, 'trip': trip})


@login_required
def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        number = trip.trip_number
        trip.delete()
        messages.success(request, f'Trip {number} deleted.')
        return redirect('trip_list')
    return redirect('trip_list')


# ════════════════════════════════════════════
# FUEL LOG
# ════════════════════════════════════════════

@login_required
def fuel_list(request):
    fuels = FuelLog.objects.all().select_related('vehicle', 'trip').order_by('-date')
    return render(request, 'operations/fuel_list.html', {'fuels': fuels})


@login_required
def fuel_add(request):
    form = FuelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Fuel log recorded successfully.')
        return redirect('fuel_list')
    return render(request, 'operations/fuel_add.html', {'form': form})


@login_required
def fuel_delete(request, pk):
    fuel = get_object_or_404(FuelLog, pk=pk)
    if request.method == 'POST':
        fuel.delete()
        messages.success(request, 'Fuel log deleted.')
        return redirect('fuel_list')
    return redirect('fuel_list')


# ════════════════════════════════════════════
# EXPENSE
# ════════════════════════════════════════════

@login_required
def expense_list(request):
    expenses = Expense.objects.all().select_related('vehicle', 'trip').order_by('-date')
    return render(request, 'operations/expense_list.html', {'expenses': expenses})


@login_required
def expense_add(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Expense recorded successfully.')
        return redirect('expense_list')
    return render(request, 'operations/expense_add.html', {'form': form})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted.')
        return redirect('expense_list')
    return redirect('expense_list')