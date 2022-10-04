from bank.services import BankService
from bank_proto import bank_pb2_grpc


def grpc_handlers(server):
    bank_pb2_grpc.add_BankServiceServicer_to_server(BankService(), server)
