# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bank_proto import bank_pb2 as bank__proto_dot_bank__pb2


class BankServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Deposit = channel.unary_unary(
                '/bank_proto.BankService/Deposit',
                request_serializer=bank__proto_dot_bank__pb2.DepositMessage.SerializeToString,
                response_deserializer=bank__proto_dot_bank__pb2.ResponseMessage.FromString,
                )
        self.Health = channel.unary_unary(
                '/bank_proto.BankService/Health',
                request_serializer=bank__proto_dot_bank__pb2.Null.SerializeToString,
                response_deserializer=bank__proto_dot_bank__pb2.Null.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/bank_proto.BankService/Withdraw',
                request_serializer=bank__proto_dot_bank__pb2.WithdrawMessage.SerializeToString,
                response_deserializer=bank__proto_dot_bank__pb2.ResponseMessage.FromString,
                )


class BankServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Health(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=bank__proto_dot_bank__pb2.DepositMessage.FromString,
                    response_serializer=bank__proto_dot_bank__pb2.ResponseMessage.SerializeToString,
            ),
            'Health': grpc.unary_unary_rpc_method_handler(
                    servicer.Health,
                    request_deserializer=bank__proto_dot_bank__pb2.Null.FromString,
                    response_serializer=bank__proto_dot_bank__pb2.Null.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=bank__proto_dot_bank__pb2.WithdrawMessage.FromString,
                    response_serializer=bank__proto_dot_bank__pb2.ResponseMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bank_proto.BankService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BankService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank_proto.BankService/Deposit',
            bank__proto_dot_bank__pb2.DepositMessage.SerializeToString,
            bank__proto_dot_bank__pb2.ResponseMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Health(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank_proto.BankService/Health',
            bank__proto_dot_bank__pb2.Null.SerializeToString,
            bank__proto_dot_bank__pb2.Null.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank_proto.BankService/Withdraw',
            bank__proto_dot_bank__pb2.WithdrawMessage.SerializeToString,
            bank__proto_dot_bank__pb2.ResponseMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)