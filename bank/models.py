"""Module docstring"""

from django.db import models


class Account(models.Model):
    """Class docstring"""
    currency = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
