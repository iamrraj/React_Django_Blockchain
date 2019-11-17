from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class InvoiceType(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    typee = models.CharField(max_length=255, help_text="Invoice Type")

    def __str__(self):
        return str(self.typee)


class Invoice(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(help_text="Date Of Invoice Add")
    plate_number = models.CharField(
        max_length=255, help_text="Plate Number Of  Cars")
    vin = models.CharField(max_length=255, help_text="Vin Number of Cars")
    invoice_number = models.CharField(
        max_length=255, help_text="Vin Number of Cars")
    invoice_type = models.ForeignKey(
        InvoiceType, models.PROTECT, null=True, related_name='invoice', blank=True, help_text="Type of invoice select from field")
    price_net = models.FloatField(help_text="Net Price of cars Trips")
    price_brutt = models.FloatField(help_text="brutto Price of cars Trips")
    description = models.CharField(
        max_length=240, help_text="Details About Car")

    def __str__(self):
        return str(self.timestamp)
