from django.contrib import admin

# Register your models here.

from .models import Car,Rental

admin.site.register(Car)
admin.site.register(Rental)
