from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    This provides the layout of info to be
    captured from a customer that makes a purchase,
    using OneToOneField to capture the user for earch order,
    links to account app's views.py and checkout app
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    postcode = models.CharField(max_length=10)
    town_city = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.email
