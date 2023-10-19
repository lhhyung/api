# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/v1/metric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'spaceone/api/monitoring/v1/metric.proto\x12\x1aspaceone.api.monitoring.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"M\n\rMetricRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\x12\x11\n\tresources\x18\x02 \x03(\t\x12\x11\n\tdomain_id\x18\n \x01(\t\"\xb7\x01\n\x11MetricDataRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\x12-\n\x0cmetric_query\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06metric\x18\x03 \x01(\t\x12\r\n\x05start\x18\n \x01(\t\x12\x0b\n\x03\x65nd\x18\x0b \x01(\t\x12\x0e\n\x06period\x18\x0c \x01(\x05\x12\x0c\n\x04stat\x18\r \x01(\t\x12\x11\n\tdomain_id\x18\x14 \x01(\t\"\x8c\x01\n\nMetricInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12%\n\x04unit\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\x0cmetric_query\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x8f\x01\n\x0bMetricsInfo\x12\x37\n\x07metrics\x18\x01 \x03(\x0b\x32&.spaceone.api.monitoring.v1.MetricInfo\x12\x34\n\x13\x61vailable_resources\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"x\n\x0eMetricDataInfo\x12*\n\x06labels\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12\'\n\x06values\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x03 \x01(\t2\x9f\x02\n\x06Metric\x12\x81\x01\n\x04list\x12).spaceone.api.monitoring.v1.MetricRequest\x1a\'.spaceone.api.monitoring.v1.MetricsInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/monitoring/v1/metric/list:\x01*\x12\x90\x01\n\x08get_data\x12-.spaceone.api.monitoring.v1.MetricDataRequest\x1a*.spaceone.api.monitoring.v1.MetricDataInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/monitoring/v1/metric/get-data:\x01*BAZ?github.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.monitoring.v1.metric_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z?github.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/v1'
  _METRIC.methods_by_name['list']._options = None
  _METRIC.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\037\"\032/monitoring/v1/metric/list:\001*'
  _METRIC.methods_by_name['get_data']._options = None
  _METRIC.methods_by_name['get_data']._serialized_options = b'\202\323\344\223\002#\"\036/monitoring/v1/metric/get-data:\001*'
  _globals['_METRICREQUEST']._serialized_start=131
  _globals['_METRICREQUEST']._serialized_end=208
  _globals['_METRICDATAREQUEST']._serialized_start=211
  _globals['_METRICDATAREQUEST']._serialized_end=394
  _globals['_METRICINFO']._serialized_start=397
  _globals['_METRICINFO']._serialized_end=537
  _globals['_METRICSINFO']._serialized_start=540
  _globals['_METRICSINFO']._serialized_end=683
  _globals['_METRICDATAINFO']._serialized_start=685
  _globals['_METRICDATAINFO']._serialized_end=805
  _globals['_METRIC']._serialized_start=808
  _globals['_METRIC']._serialized_end=1095
# @@protoc_insertion_point(module_scope)
