from django.shortcuts import render,redirect

from .models import Trip,FuelLog,Expense

from .forms import TripForm,FuelForm,ExpenseForm



# TRIP

def trip_list(request):

    trips = Trip.objects.all()

    return render(
        request,
        "operations/trip_list.html",
        {
            "trips":trips
        }
    )



def trip_add(request):

    form = TripForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("trip_list")


    return render(
        request,
        "operations/trip_add.html",
        {
            "form":form
        }
    )



def trip_edit(request,id):

    trip = Trip.objects.get(id=id)

    form = TripForm(
        request.POST or None,
        instance=trip
    )


    if form.is_valid():

        form.save()

        return redirect("trip_list")


    return render(
        request,
        "operations/trip_edit.html",
        {
            "form":form
        }
    )





# FUEL


def fuel_list(request):

    fuels = FuelLog.objects.all()


    return render(
        request,
        "operations/fuel_list.html",
        {
            "fuels":fuels
        }
    )



def fuel_add(request):

    form = FuelForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("fuel_list")


    return render(
        request,
        "operations/fuel_add.html",
        {
            "form":form
        }
    )





# EXPENSE


def expense_list(request):

    expenses = Expense.objects.all()


    return render(
        request,
        "operations/expense_list.html",
        {
            "expenses":expenses
        }
    )



def expense_add(request):

    form = ExpenseForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("expense_list")


    return render(
        request,
        "operations/expense_add.html",
        {
            "form":form
        }
    )