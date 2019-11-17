from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255, help_text="First Name Of User")
    last_name = models.CharField(
        max_length=255, help_text="Last Name Of User")
    phone = models.CharField(
        max_length=255, help_text="Phone Number oF User")
    email = models.EmailField(
        max_length=255, help_text="Email For User")
    address = models.CharField(
        max_length=255, help_text="Address OF User")
    description = models.CharField(
        max_length=255, help_text="Address OF User")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)