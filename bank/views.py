"""Module docstring"""

import json

from django.http import HttpResponse, JsonResponse

from bank.models import Account


def create_account(request):
    """Create account"""
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        currency = body['currency']
        name = body['name']
        try:
            _ = Account.objects.get(name=name)
            return JsonResponse({"result": "Error"})
        except Account.DoesNotExist as _:
            obj = Account.objects.create(name=name, currency=currency)
            obj.save()
            return JsonResponse({"result": "Ok"})
    return HttpResponse("404")


def delete_account(request):
    """Delete account"""
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        account_id = body['account_id']
        try:
            count, _ = Account.objects.get(pk=account_id).delete()
            if count == 1:
                return JsonResponse({"result": "Ok"})
            return HttpResponse("404")
        except Account.DoesNotExist as _:
            return JsonResponse({"result": "Error"})

    return HttpResponse("404")
