from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Tenant(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    address = models.TextField(blank=True)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Property(models.Model):
    property_name = models.CharField(max_length=100)
    address = models.TextField()
    bedrooms = models.PositiveIntegerField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.property_name
    
class RentDue(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100)
    due_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Rent Due for {self.property_name} - {self.due_date}"

class Payment(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()