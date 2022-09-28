import json

from django.http import HttpResponse

from bank.models import Account


def create_account(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        currency = body['currency']
        name = body['name']
        try:
            _ = Account.objects.get(name=name)
            return HttpResponse('{"result":"Error"}', content_type="application/json")
        except Exception as e:
            obj = Account.objects.create(name=name, currency=currency)
            obj.save()
            return HttpResponse('{"result":"Ok"}', content_type="application/json")


def delete_account(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        account_id = body['account_id']
        try:
            count, _ = Account.objects.get(pk=account_id).delete()
            if count == 1:
                return HttpResponse("Ok")
            else:
                return HttpResponse("404")
        except Exception as e:
            return HttpResponse("Error")
