from django import forms

from .models import Trip,FuelLog,Expense



class TripForm(forms.ModelForm):

    class Meta:

        model = Trip

        fields = "__all__"



class FuelForm(forms.ModelForm):

    class Meta:

        model = FuelLog

        fields = "__all__"



class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = "__all__"