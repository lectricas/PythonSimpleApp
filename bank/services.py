from django_grpc_framework.services import Service

from bank.models import Account
from bank_proto.bank_pb2 import ResponseMessage


class BankService(Service):

    def Deposit(self, request, context):
        try:
            account = Account.objects.get(pk=request.account_id)
            if account.currency == request.currency:
                account.amount = account.amount + request.amount
                account.save()
                return ResponseMessage(code=1, message="Added")
            else:
                return ResponseMessage(code=0, message="Wrong currency")
        except Account.DoesNotExist as _:
            return ResponseMessage(code=0, message="Account does not exists")

    def Withdraw(self, request, context):
        try:
            account = Account.objects.get(pk=request.account_id)
            if account.currency == request.currency:
                if account.amount > request.amount:
                    account.amount = account.amount - request.amount
                    account.save()
                    return ResponseMessage(code=1, message="Added")
                else:
                    return ResponseMessage(code=0, message="Not enough money")
            else:
                return ResponseMessage(code=0, message="Wrong currency")
        except Account.DoesNotExist as _:
            return ResponseMessage(code=0, message="Account does not exists")
