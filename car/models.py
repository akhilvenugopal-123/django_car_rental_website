from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    veh_reg = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    description = models.TextField()
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    
    def total_earnings(self):
        total_rentals = Rental.objects.filter(car=self).count()
        return total_rentals * self.daily_rate

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rented_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        total_earnings = self.car.total_earnings()
        return f"{self.user.username} - {self.car.name} - Rented on {self.rented_date} - Total Earnings: Rs{total_earnings}"
