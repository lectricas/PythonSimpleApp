import grpc
from bank_proto import bank_pb2, bank_pb2_grpc
from bank_proto.bank_pb2 import DepositMessage

with grpc.insecure_channel('localhost:50051') as channel:
    stub = bank_pb2_grpc.BankServiceStub(channel)
    print('----- Create -----')
    response = stub.Deposit(DepositMessage(account_id=3, amount=200, currency="RUB"))
    print(response, end='')
    print('----- List -----')
