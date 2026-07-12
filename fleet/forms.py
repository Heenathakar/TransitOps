from django import forms
from .models import Vehicle, Driver, Maintenance


# ── Shared widget helper ────────────────────────────────────────
def _input(placeholder='', extra_class=''):
    return {'class': f'form-control {extra_class}'.strip(), 'placeholder': placeholder}

def _select():
    return {'class': 'form-select'}

def _textarea(placeholder='', rows=3):
    return {'class': 'form-control', 'placeholder': placeholder, 'rows': rows}


# ════════════════════════════════════════════
class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'vehicle_number': forms.TextInput(attrs=_input('e.g. MH-12-AB-1234')),
            'vehicle_type':   forms.TextInput(attrs=_input('e.g. Truck, Bus, Van')),
            'model':          forms.TextInput(attrs=_input('e.g. Tata Prima')),
            'capacity':       forms.NumberInput(attrs=_input('Capacity in kg')),
            'status':         forms.TextInput(attrs=_input('e.g. Available, In Use')),
        }


# ════════════════════════════════════════════
class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'name':           forms.TextInput(attrs=_input('Full name')),
            'phone':          forms.TextInput(attrs=_input('+91 XXXXXXXXXX')),
            'license_number': forms.TextInput(attrs=_input('DL-XXXXXXXXXXXXXX')),
            'address':        forms.Textarea(attrs=_textarea('Complete address', rows=3)),
        }


# ════════════════════════════════════════════
class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets = {
            'vehicle':     forms.Select(attrs=_select()),
            'date':        forms.DateInput(attrs={**_input(), 'type': 'date'}),
            'description': forms.Textarea(attrs=_textarea('Describe the maintenance work', rows=3)),
            'cost':        forms.NumberInput(attrs=_input('Cost in ₹')),
        }