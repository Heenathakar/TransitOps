from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from .models import Vehicle,Driver,Maintenance

from .forms import VehicleForm,DriverForm,MaintenanceForm



# VEHICLE

def vehicle_list(request):

    vehicles = Vehicle.objects.all()

    return render(
        request,
        "fleet/vehicle_list.html",
        {
            "vehicles":vehicles
        }
    )



def vehicle_add(request):

    form = VehicleForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect("vehicle_list")


    return render(
        request,
        "fleet/vehicle_add.html",
        {
            "form":form
        }
    )



# DRIVER


def driver_list(request):

    drivers = Driver.objects.all()

    return render(
        request,
        "fleet/driver_list.html",
        {
            "drivers":drivers
        }
    )



def driver_add(request):

    form = DriverForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("driver_list")


    return render(
        request,
        "fleet/driver_add.html",
        {
            "form":form
        }
    )



# MAINTENANCE


def maintenance_list(request):

    data = Maintenance.objects.all()


    return render(
        request,
        "fleet/maintenance_list.html",
        {
            "data":data
        }
    )



def maintenance_add(request):

    form = MaintenanceForm(request.POST or None)


    if form.is_valid():

        form.save()

        return redirect("maintenance_list")


    return render(
        request,
        "fleet/maintenance_add.html",
        {
            "form":form
        }
    )