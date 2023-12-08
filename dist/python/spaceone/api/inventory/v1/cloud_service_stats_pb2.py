# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/cloud_service_stats.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3spaceone/api/inventory/v1/cloud_service_stats.proto\x12\x19spaceone.api.inventory.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xf2\x01\n\x16\x43loudServiceStatsQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x14\n\x0cquery_set_id\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x04 \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x05 \x01(\t\x12\x13\n\x0bregion_code\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x0b \x01(\t\x12\x11\n\tdomain_id\x18\x0c \x01(\t\"\xdc\x02\n\x14\x43loudServiceStatInfo\x12\x14\n\x0cquery_set_id\x18\x01 \x01(\t\x12\'\n\x06values\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04unit\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x05 \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x06 \x01(\t\x12\x13\n\x0bregion_code\x18\x07 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x08 \x01(\t\x12\x30\n\x0f\x61\x64\x64itional_info\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x15 \x01(\t\x12\x11\n\tdomain_id\x18\x16 \x01(\t\x12\x14\n\x0c\x63reated_date\x18\x1f \x01(\t\"n\n\x15\x43loudServiceStatsInfo\x12@\n\x07results\x18\x01 \x03(\x0b\x32/.spaceone.api.inventory.v1.CloudServiceStatInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"\x85\x01\n\x1d\x43loudServiceStatsAnalyzeQuery\x12;\n\x05query\x18\x01 \x01(\x0b\x32,.spaceone.api.core.v1.TimeSeriesAnalyzeQuery\x12\x14\n\x0cquery_set_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"{\n\x1a\x43loudServiceStatsStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x14\n\x0cquery_set_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t2\xd5\x03\n\x11\x43loudServiceStats\x12\x9e\x01\n\x04list\x12\x31.spaceone.api.inventory.v1.CloudServiceStatsQuery\x1a\x30.spaceone.api.inventory.v1.CloudServiceStatsInfo\"1\x82\xd3\xe4\x93\x02+\"&/inventory/v1/cloud-service-stats/list:\x01*\x12\x92\x01\n\x07\x61nalyze\x12\x38.spaceone.api.inventory.v1.CloudServiceStatsAnalyzeQuery\x1a\x17.google.protobuf.Struct\"4\x82\xd3\xe4\x93\x02.\")/inventory/v1/cloud-service-stats/analyze:\x01*\x12\x89\x01\n\x04stat\x12\x35.spaceone.api.inventory.v1.CloudServiceStatsStatQuery\x1a\x17.google.protobuf.Struct\"1\x82\xd3\xe4\x93\x02+\"&/inventory/v1/cloud-service-stats/stat:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory.v1.cloud_service_stats_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/inventory/v1'
  _globals['_CLOUDSERVICESTATS'].methods_by_name['list']._options = None
  _globals['_CLOUDSERVICESTATS'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002+\"&/inventory/v1/cloud-service-stats/list:\001*'
  _globals['_CLOUDSERVICESTATS'].methods_by_name['analyze']._options = None
  _globals['_CLOUDSERVICESTATS'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002.\")/inventory/v1/cloud-service-stats/analyze:\001*'
  _globals['_CLOUDSERVICESTATS'].methods_by_name['stat']._options = None
  _globals['_CLOUDSERVICESTATS'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002+\"&/inventory/v1/cloud-service-stats/stat:\001*'
  _globals['_CLOUDSERVICESTATSQUERY']._serialized_start=177
  _globals['_CLOUDSERVICESTATSQUERY']._serialized_end=419
  _globals['_CLOUDSERVICESTATINFO']._serialized_start=422
  _globals['_CLOUDSERVICESTATINFO']._serialized_end=770
  _globals['_CLOUDSERVICESTATSINFO']._serialized_start=772
  _globals['_CLOUDSERVICESTATSINFO']._serialized_end=882
  _globals['_CLOUDSERVICESTATSANALYZEQUERY']._serialized_start=885
  _globals['_CLOUDSERVICESTATSANALYZEQUERY']._serialized_end=1018
  _globals['_CLOUDSERVICESTATSSTATQUERY']._serialized_start=1020
  _globals['_CLOUDSERVICESTATSSTATQUERY']._serialized_end=1143
  _globals['_CLOUDSERVICESTATS']._serialized_start=1146
  _globals['_CLOUDSERVICESTATS']._serialized_end=1615
# @@protoc_insertion_point(module_scope)
