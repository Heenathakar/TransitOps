from django import forms
from .models import Trip, FuelLog, Expense


# ── Shared widget helper ────────────────────────────────────────
def _input(placeholder='', type_='text'):
    attrs = {'class': 'form-control', 'placeholder': placeholder}
    if type_ != 'text':
        attrs['type'] = type_
    return attrs

def _select():
    return {'class': 'form-select'}

def _textarea(placeholder='', rows=3):
    return {'class': 'form-control', 'placeholder': placeholder, 'rows': rows}


# ════════════════════════════════════════════
class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'trip_number':       forms.TextInput(attrs=_input('e.g. TR-0001')),
            'source':            forms.TextInput(attrs=_input('Origin city / depot')),
            'destination':       forms.TextInput(attrs=_input('Destination city / depot')),
            'vehicle':           forms.Select(attrs=_select()),
            'driver':            forms.Select(attrs=_select()),
            'cargo_weight':      forms.NumberInput(attrs=_input('Weight in kg')),
            'planned_distance':  forms.NumberInput(attrs=_input('Distance in km')),
            'actual_distance':   forms.NumberInput(attrs=_input('Actual km (optional)')),
            'fuel_used':         forms.NumberInput(attrs=_input('Liters used (optional)')),
            'status':            forms.Select(attrs=_select()),
            'start_date':        forms.DateInput(attrs={**_input(), 'type': 'date'}),
            'end_date':          forms.DateInput(attrs={**_input(), 'type': 'date'}),
        }


# ════════════════════════════════════════════
class FuelForm(forms.ModelForm):

    class Meta:
        model = FuelLog
        fields = '__all__'
        widgets = {
            'vehicle': forms.Select(attrs=_select()),
            'trip':    forms.Select(attrs=_select()),
            'liters':  forms.NumberInput(attrs=_input('Liters filled')),
            'cost':    forms.NumberInput(attrs=_input('Total cost in ₹')),
            'date':    forms.DateInput(attrs={**_input(), 'type': 'date'}),
        }


# ════════════════════════════════════════════
class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'vehicle':      forms.Select(attrs=_select()),
            'trip':         forms.Select(attrs=_select()),
            'expense_type': forms.Select(attrs=_select()),
            'amount':       forms.NumberInput(attrs=_input('Amount in ₹')),
            'remarks':      forms.Textarea(attrs=_textarea('Optional remarks', rows=2)),
            'date':         forms.DateInput(attrs={**_input(), 'type': 'date'}),
        }