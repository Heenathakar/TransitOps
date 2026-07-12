from django.db import models
from fleet.models import Vehicle, Driver


# ----------------------------
# Trip Model
# ----------------------------
class Trip(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Completed', 'Completed'), 
        ('Cancelled', 'Cancelled'),
    ]

    trip_number = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='trips'
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='trips'
    )

    cargo_weight = models.DecimalField(max_digits=10, decimal_places=2)

    planned_distance = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    actual_distance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    fuel_used = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.trip_number


# ----------------------------
# Fuel Log Model
# ----------------------------
class FuelLog(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE
    )

    liters = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.vehicle} - {self.date}"


# ----------------------------
# Expense Model
# ----------------------------
class Expense(models.Model):

    EXPENSE_CHOICES = [
        ('Fuel', 'Fuel'),
        ('Toll', 'Toll'),
        ('Repair', 'Repair'),
        ('Salary', 'Salary'),
        ('Parking', 'Parking'),
        ('Other', 'Other'),
    ]

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE
    )

    expense_type = models.CharField(
        max_length=50,
        choices=EXPENSE_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.expense_type} - ₹{self.amount}"