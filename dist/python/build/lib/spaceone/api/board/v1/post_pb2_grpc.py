# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.board.v1 import post_pb2 as spaceone_dot_api_dot_board_dot_v1_dot_post__pb2

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
        + f' but the generated code in spaceone/api/board/v1/post_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PostStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.board.v1.Post/create',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.board.v1.Post/update',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.UpdatePostRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
                _registered_method=True)
        self.send = channel.unary_unary(
                '/spaceone.api.board.v1.Post/send',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.board.v1.Post/delete',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.board.v1.Post/get',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.board.v1.Post/list',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.board.v1.Post/stat',
                request_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class PostServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Creates a new Post under a specific Board. You must specify the `board_id`, `title`, and `contents`. The parameter `category` is not required but can be set in the scope of `categories` specified in the parent Board. You can make the new Post pinned or pop up by adjusting the parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Updates a specific Post. You can make changes in Post settings, except `board_id`, `post_id`, and `domain_id`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send(self, request, context):
        """Not Implemented
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Deletes a specific Post. You must specify the `post_id` of the Post to delete, and the `board_id` of the Board where the child Post to delete belongs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all Posts. You can use a query to get a filtered list of Posts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.CreatePostRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.UpdatePostRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.SerializeToString,
            ),
            'send': grpc.unary_unary_rpc_method_handler(
                    servicer.send,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.board.v1.Post', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.board.v1.Post', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Post(object):
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
            '/spaceone.api.board.v1.Post/create',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.CreatePostRequest.SerializeToString,
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
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
            '/spaceone.api.board.v1.Post/update',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.UpdatePostRequest.SerializeToString,
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
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
    def send(request,
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
            '/spaceone.api.board.v1.Post/send',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
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
            '/spaceone.api.board.v1.Post/delete',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
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
            '/spaceone.api.board.v1.Post/get',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostRequest.SerializeToString,
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostInfo.FromString,
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
            '/spaceone.api.board.v1.Post/list',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostSearchQuery.SerializeToString,
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostsInfo.FromString,
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
            '/spaceone.api.board.v1.Post/stat',
            spaceone_dot_api_dot_board_dot_v1_dot_post__pb2.PostStatQuery.SerializeToString,
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
