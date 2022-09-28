"""Module docstring"""

from django.urls import path
from .views import create_account
from .views import delete_account

app_name = "bank"

urlpatterns = [
    path('bank/create', create_account, name = "create_account"),
    path('bank/delete', delete_account, name = "delete_account"),
]
