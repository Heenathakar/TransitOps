from django.db import models


class Vehicle(models.Model):

    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    status = models.CharField(max_length=50)


    def __str__(self):
        return self.vehicle_number



class Driver(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    address = models.TextField()


    def __str__(self):
        return self.name



class Maintenance(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    description = models.TextField()

    cost = models.FloatField()


    def __str__(self):
        return self.vehicle.vehicle_number