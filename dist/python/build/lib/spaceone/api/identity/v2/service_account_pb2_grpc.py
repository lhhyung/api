# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.identity.v2 import service_account_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2


class ServiceAccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/create',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.CreateServiceAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.UpdateServiceAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
                )
        self.change_trusted_service_account = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/change_trusted_service_account',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ChangeTrustedAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/delete',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/get',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/list',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountsInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.identity.v2.ServiceAccount/stat',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class ServiceAccountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_trusted_service_account(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceAccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.CreateServiceAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.UpdateServiceAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.SerializeToString,
            ),
            'change_trusted_service_account': grpc.unary_unary_rpc_method_handler(
                    servicer.change_trusted_service_account,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ChangeTrustedAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v2.ServiceAccount', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceAccount(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/create',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.CreateServiceAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/update',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.UpdateServiceAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_trusted_service_account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/change_trusted_service_account',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ChangeTrustedAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/delete',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/get',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/list',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountSearchQuery.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountsInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v2.ServiceAccount/stat',
            spaceone_dot_api_dot_identity_dot_v2_dot_service__account__pb2.ServiceAccountStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
