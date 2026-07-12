from django import forms

from .models import Vehicle,Driver,Maintenance



class VehicleForm(forms.ModelForm):

    class Meta:

        model = Vehicle

        fields = "__all__"



class DriverForm(forms.ModelForm):

    class Meta:

        model = Driver

        fields = "__all__"



class MaintenanceForm(forms.ModelForm):

    class Meta:

        model = Maintenance

        fields = "__all__"