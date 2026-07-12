from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('Fleet Manager', 'Fleet Manager'),
        ('Dispatcher', 'Dispatcher'),
        ('Safety Officer', 'Safety Officer'),
        ('Financial Analyst', 'Financial Analyst'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name