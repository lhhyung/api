# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.identity.v2 import workspace_group_details_pb2 as spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2

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
        + f' but the generated code in spaceone/api/identity/v2/workspace_group_details_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class WorkspaceGroupDetailsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.UpdateWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/delete',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.DeleteWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.add_workspaces = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/add_workspaces',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
                _registered_method=True)
        self.remove_workspaces = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_workspaces',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
                _registered_method=True)
        self.find_users = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/find_users',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsFindRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsUsersSummaryInfo.FromString,
                _registered_method=True)
        self.add_users = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/add_users',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.AddUsersWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
                _registered_method=True)
        self.remove_users = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_users',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.RemoveUsersWorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
                _registered_method=True)
        self.get_workspace_groups = channel.unary_unary(
                '/spaceone.api.identity.v2.WorkspaceGroupDetails/get_workspace_groups',
                request_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupsDetailsInfo.FromString,
                _registered_method=True)


class WorkspaceGroupDetailsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_workspaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_workspaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def find_users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_workspace_groups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkspaceGroupDetailsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.UpdateWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.DeleteWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'add_workspaces': grpc.unary_unary_rpc_method_handler(
                    servicer.add_workspaces,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.SerializeToString,
            ),
            'remove_workspaces': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_workspaces,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.SerializeToString,
            ),
            'find_users': grpc.unary_unary_rpc_method_handler(
                    servicer.find_users,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsFindRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsUsersSummaryInfo.SerializeToString,
            ),
            'add_users': grpc.unary_unary_rpc_method_handler(
                    servicer.add_users,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.AddUsersWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.SerializeToString,
            ),
            'remove_users': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_users,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.RemoveUsersWorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.SerializeToString,
            ),
            'get_workspace_groups': grpc.unary_unary_rpc_method_handler(
                    servicer.get_workspace_groups,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupsDetailsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v2.WorkspaceGroupDetails', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.identity.v2.WorkspaceGroupDetails', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WorkspaceGroupDetails(object):
    """Missing associated documentation comment in .proto file."""

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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/update',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.UpdateWorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/delete',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.DeleteWorkspaceGroupDetailsRequest.SerializeToString,
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
    def add_workspaces(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/add_workspaces',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
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
    def remove_workspaces(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_workspaces',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspacesWorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
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
    def find_users(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/find_users',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsFindRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsUsersSummaryInfo.FromString,
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
    def add_users(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/add_users',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.AddUsersWorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
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
    def remove_users(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_users',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.RemoveUsersWorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsInfo.FromString,
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
    def get_workspace_groups(request,
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
            '/spaceone.api.identity.v2.WorkspaceGroupDetails/get_workspace_groups',
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupDetailsRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v2_dot_workspace__group__details__pb2.WorkspaceGroupsDetailsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
