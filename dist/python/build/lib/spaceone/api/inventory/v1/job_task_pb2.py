# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/job_task.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.inventory.v1 import collector_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_collector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(spaceone/api/inventory/v1/job_task.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a)spaceone/api/inventory/v1/collector.proto\"8\n\x0eJobTaskRequest\x12\x13\n\x0bjob_task_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"I\n\x11GetJobTaskRequest\x12\x13\n\x0bjob_task_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xfe\x02\n\x0cJobTaskQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x13\n\x0bjob_task_id\x18\x02 \x01(\t\x12\x45\n\x06status\x18\x03 \x01(\x0e\x32\x35.spaceone.api.inventory.v1.JobTaskQuery.JobTaskStatus\x12\x0e\n\x06job_id\x18\x04 \x01(\t\x12\x11\n\tsecret_id\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x1a\n\x12service_account_id\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\"n\n\rJobTaskStatus\x12\x17\n\x13JOB_TASK_STATE_NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08\x43\x41NCELED\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\x0b\n\x07\x46\x41ILURE\x10\x05\"\xbb\x04\n\x0bJobTaskInfo\x12\x13\n\x0bjob_task_id\x18\x01 \x01(\t\x12\x44\n\x06status\x18\x02 \x01(\x0e\x32\x34.spaceone.api.inventory.v1.JobTaskInfo.JobTaskStatus\x12\x15\n\rcreated_count\x18\x03 \x01(\x05\x12\x15\n\rupdated_count\x18\x04 \x01(\x05\x12\x15\n\rfailure_count\x18\x05 \x01(\x05\x12\x15\n\rdeleted_count\x18\x06 \x01(\x05\x12\x1a\n\x12\x64isconnected_count\x18\x07 \x01(\x05\x12\x34\n\x06\x65rrors\x18\t \x03(\x0b\x32$.spaceone.api.inventory.v1.ErrorInfo\x12\x0e\n\x06job_id\x18\x0b \x01(\t\x12\x11\n\tsecret_id\x18\x0c \x01(\t\x12\x10\n\x08provider\x18\r \x01(\t\x12\x1a\n\x12service_account_id\x18\x0e \x01(\t\x12\x12\n\nproject_id\x18\x0f \x01(\t\x12\x11\n\tdomain_id\x18\x10 \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\t\x12\x12\n\nstarted_at\x18\x16 \x01(\t\x12\x13\n\x0b\x66inished_at\x18\x17 \x01(\t\"n\n\rJobTaskStatus\x12\x17\n\x13JOB_TASK_STATE_NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08\x43\x41NCELED\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\x0b\n\x07\x46\x41ILURE\x10\x05\"\\\n\x0cJobTasksInfo\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.spaceone.api.inventory.v1.JobTaskInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"[\n\x10JobTaskStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xfe\x03\n\x07JobTask\x12u\n\x06\x64\x65lete\x12).spaceone.api.inventory.v1.JobTaskRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\"\x1d/inventory/v1/job-task/delete:\x01*\x12\x82\x01\n\x03get\x12,.spaceone.api.inventory.v1.GetJobTaskRequest\x1a&.spaceone.api.inventory.v1.JobTaskInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/inventory/v1/job-task/get:\x01*\x12\x80\x01\n\x04list\x12\'.spaceone.api.inventory.v1.JobTaskQuery\x1a\'.spaceone.api.inventory.v1.JobTasksInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/inventory/v1/job-task/list:\x01*\x12t\n\x04stat\x12+.spaceone.api.inventory.v1.JobTaskStatQuery\x1a\x17.google.protobuf.Struct\"&\x82\xd3\xe4\x93\x02 \"\x1b/inventory/v1/job-task/stat:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory.v1.job_task_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1'
  _globals['_JOBTASK'].methods_by_name['delete']._options = None
  _globals['_JOBTASK'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\"\"\035/inventory/v1/job-task/delete:\001*'
  _globals['_JOBTASK'].methods_by_name['get']._options = None
  _globals['_JOBTASK'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\037\"\032/inventory/v1/job-task/get:\001*'
  _globals['_JOBTASK'].methods_by_name['list']._options = None
  _globals['_JOBTASK'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002 \"\033/inventory/v1/job-task/list:\001*'
  _globals['_JOBTASK'].methods_by_name['stat']._options = None
  _globals['_JOBTASK'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002 \"\033/inventory/v1/job-task/stat:\001*'
  _globals['_JOBTASKREQUEST']._serialized_start=237
  _globals['_JOBTASKREQUEST']._serialized_end=293
  _globals['_GETJOBTASKREQUEST']._serialized_start=295
  _globals['_GETJOBTASKREQUEST']._serialized_end=368
  _globals['_JOBTASKQUERY']._serialized_start=371
  _globals['_JOBTASKQUERY']._serialized_end=753
  _globals['_JOBTASKQUERY_JOBTASKSTATUS']._serialized_start=643
  _globals['_JOBTASKQUERY_JOBTASKSTATUS']._serialized_end=753
  _globals['_JOBTASKINFO']._serialized_start=756
  _globals['_JOBTASKINFO']._serialized_end=1327
  _globals['_JOBTASKINFO_JOBTASKSTATUS']._serialized_start=643
  _globals['_JOBTASKINFO_JOBTASKSTATUS']._serialized_end=753
  _globals['_JOBTASKSINFO']._serialized_start=1329
  _globals['_JOBTASKSINFO']._serialized_end=1421
  _globals['_JOBTASKSTATQUERY']._serialized_start=1423
  _globals['_JOBTASKSTATQUERY']._serialized_end=1514
  _globals['_JOBTASK']._serialized_start=1517
  _globals['_JOBTASK']._serialized_end=2027
# @@protoc_insertion_point(module_scope)
