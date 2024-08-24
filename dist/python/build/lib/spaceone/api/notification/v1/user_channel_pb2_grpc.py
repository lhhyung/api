# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.notification.v1 import user_channel_pb2 as spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2

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
        + f' but the generated code in spaceone/api/notification/v1/user_channel_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UserChannelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/create',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.CreateUserChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/update',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.set_schedule = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/set_schedule',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelScheduleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.set_subscription = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/set_subscription',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelSubscriptionRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/enable',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/disable',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/delete',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/get',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/list',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.notification.v1.UserChannel/stat',
                request_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class UserChannelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new UserChannel. A UserChannel is a channel that delivers a Notification to users when the Notification is created. When creating a UserChannel, one Protocol must be selected, and an Notification is dispatched via the selected Protocol.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific UserChannel. A UserChannel that has already been configured cannot be changed. Instead, the data required for dispatching Notifications to a UserChannel can be updated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_schedule(self, request, context):
        """Sets a schedule for a UserChannel. A schedule defines the time to receive a Notification. When a Notification is created, you can set the day of the week and time you want to receive it. When you set the day of the week, you can receive a notification only on the day of the week you set. If you also set the start time and end time with the day of the week, you can receive a Notification only at the scheduled time on the day of the week you set. If there is no schedule set in a UserChannel, Notifications will be dispatched at all times via the UserChannel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_subscription(self, request, context):
        """Sets a subscription for a UserChannel. A subscription is a topic for channels to subscribe to and get notified about. If a UserChannel has subscriptions, a Notification is dispatched only if the topic of the Notification is the same as the one set in the subscriptions. If there is no subscription in a UserChannel, all Notifications will be dispatched.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """Enables a specific UserChannel. If a UserChannel is enabled, the UserChannel can be used and the Notification can be dispatched. Even if a UserChannel is enabled, if the Protocol used in the UserChannel is disabled, the Notification is not dispatched.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
        """Disables a specific UserChannel. If a UserChannel is disabled, the Notification is not dispatched, even if it is created.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific UserChannel. You must specify the `user_channel_id` of the UserChannel to delete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific UserChannel. Prints detailed information about the UserChannel, including the Protocol configured and the Notification settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all UserChannels. You can use a query to get a filtered list of UserChannels.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserChannelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.CreateUserChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'set_schedule': grpc.unary_unary_rpc_method_handler(
                    servicer.set_schedule,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelScheduleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'set_subscription': grpc.unary_unary_rpc_method_handler(
                    servicer.set_subscription,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelSubscriptionRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.notification.v1.UserChannel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.notification.v1.UserChannel', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserChannel(object):
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
            '/spaceone.api.notification.v1.UserChannel/create',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.CreateUserChannelRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/update',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
    def set_schedule(request,
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
            '/spaceone.api.notification.v1.UserChannel/set_schedule',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelScheduleRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
    def set_subscription(request,
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
            '/spaceone.api.notification.v1.UserChannel/set_subscription',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UpdateUserChannelSubscriptionRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/enable',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/disable',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/delete',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
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
            '/spaceone.api.notification.v1.UserChannel/get',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelRequest.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/list',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelQuery.SerializeToString,
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelsInfo.FromString,
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
            '/spaceone.api.notification.v1.UserChannel/stat',
            spaceone_dot_api_dot_notification_dot_v1_dot_user__channel__pb2.UserChannelStatQuery.SerializeToString,
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
