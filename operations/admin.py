from django.contrib import admin

from .models import Trip,FuelLog,Expense


admin.site.register(Trip)

admin.site.register(FuelLog)

admin.site.register(Expense)