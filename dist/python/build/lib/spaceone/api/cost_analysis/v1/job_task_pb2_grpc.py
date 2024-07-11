# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.cost_analysis.v1 import job_task_pb2 as spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2

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
        + f' but the generated code in spaceone/api/cost_analysis/v1/job_task_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class JobTaskStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.JobTask/get',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.JobTask/list',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTasksInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.JobTask/stat',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class JobTaskServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get(self, request, context):
        """Gets a specific JobTask. Prints detailed information about the JobTask, including the relevant resources: DataSource and Job. The criteria used for dividing a Job into JobTasks can be found in the DataSource used, but the total count of divided JobTasks can be found by this method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Gets a list of all JobTasks. You can use a query to get a filtered list of JobTasks.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JobTaskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTasksInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_analysis.v1.JobTask', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.cost_analysis.v1.JobTask', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class JobTask(object):
    """Missing associated documentation comment in .proto file."""

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
            '/spaceone.api.cost_analysis.v1.JobTask/get',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskInfo.FromString,
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
            '/spaceone.api.cost_analysis.v1.JobTask/list',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskQuery.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTasksInfo.FromString,
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
            '/spaceone.api.cost_analysis.v1.JobTask/stat',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__task__pb2.JobTaskStatQuery.SerializeToString,
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
