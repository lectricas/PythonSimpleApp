from django.http import HttpResponse
from django.conf import settings
import json
from bank.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers


# Create your views here.

def deposit(request):
    # db = settings.DATABASE
    # accounts = db.accounts
    # amount = request.GET.get('amount', None)
    # currency = request.GET.get('currency', None)
    # account_number = request.GET.get('account_number', None)

    # deposit = Deposit(account_number, currency, amount)

    return HttpResponse("Deposit " + " hello")


def withdraw(request):
    # amount = request.GET.get('amount', None)
    # currency = request.GET.get('currency', None)
    # account_number = request.GET.get('account_number', None)
    return HttpResponse("Withdraw " + "hello")


def create_account(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        currency = body['currency']
        name = body['name']
        try:
            _ = Account.objects.get(name=name)  # так?
            return HttpResponse("Exists")
        except Exception as e:
            obj = Account.objects.create(name=name, currency=currency)
            obj.save()
            return HttpResponse("Ok")


def delete_account(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        account_id = body['account_id']
        try:
            count, _ = Account.objects.get(pk=account_id).delete()  # или так?
            if count == 1:
                return render(HttpResponse("Deleted"))
            else:
                return render(HttpResponse("404"))
        except Exception as e:
            return render(HttpResponse("Does not exists"))

    return render(HttpResponse("Deleted"))