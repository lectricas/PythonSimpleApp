"""Module docstring"""

from django.db import models


class Account(models.Model):
    """Class docstring"""
    currency = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=3, max_digits=10, default=0)
