# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.secret.v1 import secret_pb2 as spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/secret/v1/secret_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SecretStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/create',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.CreateSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/update',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/delete',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/enable',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/disable',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
                _registered_method=True)
        self.update_data = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/update_data',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretDataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get_data = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/get_data',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.GetSecretDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretDataInfo.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/get',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/list',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.secret.v1.Secret/stat',
                request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class SecretServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Create a new secret.
        Created secret is encrypted and stored securely.
        It can be used to link to a trusted secret if you request it with 'trusted_secret_id' in the parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific secret's information.
        You can only change the 'name' and 'tags', and to change the data you must use the update_data API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific secret.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """Enables a specific secret.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """Disables a specific secret.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_data(self, request, context):
        """Updates a specific secret's data.
        Updated secret is encrypted and stored securely.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_data(self, request, context):
        """Get a specific secret's data.
        This API is for internal system use only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Get a specific secret's information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Queries a list of secrets.
        You can use a query to get a filtered list of secrets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecretServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.CreateSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
            ),
            'update_data': grpc.unary_unary_rpc_method_handler(
                    servicer.update_data,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretDataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get_data': grpc.unary_unary_rpc_method_handler(
                    servicer.get_data,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.GetSecretDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretDataInfo.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.secret.v1.Secret', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.secret.v1.Secret', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Secret(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/create',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.CreateSecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/update',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/delete',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def enable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/enable',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/disable',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def update_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/update_data',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretDataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/get_data',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.GetSecretDataRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretDataInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/get',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/list',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretQuery.SerializeToString,
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.secret.v1.Secret/stat',
            spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
