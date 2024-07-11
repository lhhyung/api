# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.inventory.v1 import collector_rule_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2

GRPC_GENERATED_VERSION = '1.65.0'
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
        + f' but the generated code in spaceone/api/inventory/v1/collector_rule_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class CollectorRuleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CreateCollectorRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.UpdateCollectorRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
                _registered_method=True)
        self.change_order = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/change_order',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.ChangeCollectorRuleOrderRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRulesInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.CollectorRule/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class CollectorRuleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new CollectorRule. When creating the cloud service, this method can apply two types of conditions: mapping projects where the cloud service incurred to the Cloud Service, and mapping cloud service accounts to the Cloud Service. By adjusting the `condition_policy` parameter, the CollectorRule can be applied when all conditions are met, applied when any of the conditions are met, or always applied regardless of whether the conditions are met.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific CollectorRule. You can make changes in CollectorRule settings, including filtering conditions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_order(self, request, context):
        """Changes the priority order of the CollectorRules to apply. If there are multiple CollectorRules applied in a specific service account, the priority order of the resources is required. This method changes the priority order to apply CollectorRules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific CollectorRule. You must specify the `collector_rule_id` of the CollectorRule to delete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific CollectorRule. Prints detailed information about the CollectorRule, including  `conditions_policy` and conditions applied to Collector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all CollectorRules. You can use a query to get a filtered list of CollectorRules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectorRuleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CreateCollectorRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.UpdateCollectorRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.SerializeToString,
            ),
            'change_order': grpc.unary_unary_rpc_method_handler(
                    servicer.change_order,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.ChangeCollectorRuleOrderRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRulesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.CollectorRule', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.inventory.v1.CollectorRule', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CollectorRule(object):
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
            '/spaceone.api.inventory.v1.CollectorRule/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CreateCollectorRuleRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
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
            '/spaceone.api.inventory.v1.CollectorRule/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.UpdateCollectorRuleRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
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
    def change_order(request,
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
            '/spaceone.api.inventory.v1.CollectorRule/change_order',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.ChangeCollectorRuleOrderRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
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
            '/spaceone.api.inventory.v1.CollectorRule/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.SerializeToString,
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
            '/spaceone.api.inventory.v1.CollectorRule/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleInfo.FromString,
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
            '/spaceone.api.inventory.v1.CollectorRule/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRulesInfo.FromString,
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
            '/spaceone.api.inventory.v1.CollectorRule/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_collector__rule__pb2.CollectorRuleStatQuery.SerializeToString,
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
