from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Campaign(models.Model):
    campname = models.CharField(
        max_length=255, help_text="Campaign Name" , null=True, blank=True)
    description = models.CharField(
        max_length=255, null=True, blank=True)
    camptype = models.CharField(
        max_length=255, null=True, blank=True,help_text="Campaign Type")
    campdate = models.DateField(help_text="Campaign Type Date", null=True, blank=True)
    campperiodfrom = models.DateField(help_text="Campaign  Period Type From Date", null=True, blank=True)
    campperiodto = models.DateField(help_text="Campaign  Period Type To Date", null=True, blank=True)
    parameters = models.CharField(
        max_length=255, null=True, blank=True, help_text="Parameters To improve")
    candidate = models.CharField(
        max_length=255, null=True, blank=True, help_text="Select Candidate")
    prize = models.CharField(
        max_length=255, null=True, blank=True, help_text="Prize Type")
    prizetype = models.IntegerField(null=True, blank=True, help_text="Number OF Prize")

    title = models.CharField(
        max_length=255, null=True, blank=True, help_text="Title 1")
    title1 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Title 2")
    title2 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Title 3")

    prizetype = models.CharField(
        max_length=255, null=True, blank=True, help_text="Prize Type 1")
    prizetype1 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Prize Type 2")
    prizetype2 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Prize Type 3")
    
    prizemoney = models.IntegerField(null=True, blank=True, help_text="Prize Money 1")
    prizemoney1 = models.IntegerField(null=True, blank=True, help_text="Prize Money 2")
    prizemoney2 = models.IntegerField(null=True, blank=True, help_text="Prize Money 3")

    prizequantity = models.IntegerField(null=True, blank=True, help_text="Number oF Prize Quantity 1")
    prizequantity1 = models.IntegerField(null=True, blank=True, help_text="Number oF Prize Quantity 2")
    prizequantity2 = models.IntegerField(null=True, blank=True, help_text="Number oF Prize Quantity 3")

    rank = models.CharField(
        max_length=255, null=True, blank=True, help_text="Rank 1")
    rank1 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Rank 2")
    rank2 = models.CharField(
        max_length=255, null=True, blank=True, help_text="Rank 3")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)




















