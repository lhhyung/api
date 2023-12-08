# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/v1/project_alert_config.proto
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
from spaceone.api.monitoring.v1 import escalation_policy_pb2 as spaceone_dot_api_dot_monitoring_dot_v1_dot_escalation__policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5spaceone/api/monitoring/v1/project_alert_config.proto\x12\x1aspaceone.api.monitoring.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a\x32spaceone/api/monitoring/v1/escalation_policy.proto\"\xaa\x02\n\x0c\x41lertOptions\x12T\n\x14notification_urgency\x18\x01 \x01(\x0e\x32\x36.spaceone.api.monitoring.v1.AlertOptions.UrgencyOption\x12N\n\rrecovery_mode\x18\x02 \x01(\x0e\x32\x37.spaceone.api.monitoring.v1.AlertOptions.RecoveryOption\"9\n\rUrgencyOption\x12\x10\n\x0cURGENCY_NONE\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\r\n\tHIGH_ONLY\x10\x02\"9\n\x0eRecoveryOption\x12\x11\n\rRECOVERY_NONE\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\x12\n\n\x06MANUAL\x10\x02\"\xa1\x01\n\x1f\x43reateProjectAlertConfigRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x1c\n\x14\x65scalation_policy_id\x18\x02 \x01(\t\x12\x39\n\x07options\x18\x03 \x01(\x0b\x32(.spaceone.api.monitoring.v1.AlertOptions\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\xa1\x01\n\x1fUpdateProjectAlertConfigRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x1c\n\x14\x65scalation_policy_id\x18\x02 \x01(\t\x12\x39\n\x07options\x18\x03 \x01(\x0b\x32(.spaceone.api.monitoring.v1.AlertOptions\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"B\n\x19ProjectAlertConfigRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"S\n\x1cGetProjectAlertConfigRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\x8a\x01\n\x17ProjectAlertConfigQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1c\n\x14\x65scalation_policy_id\x18\x03 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\xe0\x01\n\x16ProjectAlertConfigInfo\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x39\n\x07options\x18\x02 \x01(\x0b\x32(.spaceone.api.monitoring.v1.AlertOptions\x12P\n\x16\x65scalation_policy_info\x18\x03 \x01(\x0b\x32\x30.spaceone.api.monitoring.v1.EscalationPolicyInfo\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\t\"s\n\x17ProjectAlertConfigsInfo\x12\x43\n\x07results\x18\x01 \x03(\x0b\x32\x32.spaceone.api.monitoring.v1.ProjectAlertConfigInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"f\n\x1bProjectAlertConfigStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xed\x07\n\x12ProjectAlertConfig\x12\xb0\x01\n\x06\x63reate\x12;.spaceone.api.monitoring.v1.CreateProjectAlertConfigRequest\x1a\x32.spaceone.api.monitoring.v1.ProjectAlertConfigInfo\"5\x82\xd3\xe4\x93\x02/\"*/monitoring/v1/project-alert-config/create:\x01*\x12\xb0\x01\n\x06update\x12;.spaceone.api.monitoring.v1.UpdateProjectAlertConfigRequest\x1a\x32.spaceone.api.monitoring.v1.ProjectAlertConfigInfo\"5\x82\xd3\xe4\x93\x02/\"*/monitoring/v1/project-alert-config/update:\x01*\x12\x8e\x01\n\x06\x64\x65lete\x12\x35.spaceone.api.monitoring.v1.ProjectAlertConfigRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"*/monitoring/v1/project-alert-config/delete:\x01*\x12\xa7\x01\n\x03get\x12\x38.spaceone.api.monitoring.v1.GetProjectAlertConfigRequest\x1a\x32.spaceone.api.monitoring.v1.ProjectAlertConfigInfo\"2\x82\xd3\xe4\x93\x02,\"\'/monitoring/v1/project-alert-config/get:\x01*\x12\xa5\x01\n\x04list\x12\x33.spaceone.api.monitoring.v1.ProjectAlertConfigQuery\x1a\x33.spaceone.api.monitoring.v1.ProjectAlertConfigsInfo\"3\x82\xd3\xe4\x93\x02-\"(/monitoring/v1/project-alert-config/list:\x01*\x12\x8d\x01\n\x04stat\x12\x37.spaceone.api.monitoring.v1.ProjectAlertConfigStatQuery\x1a\x17.google.protobuf.Struct\"3\x82\xd3\xe4\x93\x02-\"(/monitoring/v1/project-alert-config/stat:\x01*BAZ?github.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.monitoring.v1.project_alert_config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/v1'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['create']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002/\"*/monitoring/v1/project-alert-config/create:\001*'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['update']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002/\"*/monitoring/v1/project-alert-config/update:\001*'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['delete']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002/\"*/monitoring/v1/project-alert-config/delete:\001*'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['get']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002,\"\'/monitoring/v1/project-alert-config/get:\001*'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['list']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002-\"(/monitoring/v1/project-alert-config/list:\001*'
  _globals['_PROJECTALERTCONFIG'].methods_by_name['stat']._options = None
  _globals['_PROJECTALERTCONFIG'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002-\"(/monitoring/v1/project-alert-config/stat:\001*'
  _globals['_ALERTOPTIONS']._serialized_start=261
  _globals['_ALERTOPTIONS']._serialized_end=559
  _globals['_ALERTOPTIONS_URGENCYOPTION']._serialized_start=443
  _globals['_ALERTOPTIONS_URGENCYOPTION']._serialized_end=500
  _globals['_ALERTOPTIONS_RECOVERYOPTION']._serialized_start=502
  _globals['_ALERTOPTIONS_RECOVERYOPTION']._serialized_end=559
  _globals['_CREATEPROJECTALERTCONFIGREQUEST']._serialized_start=562
  _globals['_CREATEPROJECTALERTCONFIGREQUEST']._serialized_end=723
  _globals['_UPDATEPROJECTALERTCONFIGREQUEST']._serialized_start=726
  _globals['_UPDATEPROJECTALERTCONFIGREQUEST']._serialized_end=887
  _globals['_PROJECTALERTCONFIGREQUEST']._serialized_start=889
  _globals['_PROJECTALERTCONFIGREQUEST']._serialized_end=955
  _globals['_GETPROJECTALERTCONFIGREQUEST']._serialized_start=957
  _globals['_GETPROJECTALERTCONFIGREQUEST']._serialized_end=1040
  _globals['_PROJECTALERTCONFIGQUERY']._serialized_start=1043
  _globals['_PROJECTALERTCONFIGQUERY']._serialized_end=1181
  _globals['_PROJECTALERTCONFIGINFO']._serialized_start=1184
  _globals['_PROJECTALERTCONFIGINFO']._serialized_end=1408
  _globals['_PROJECTALERTCONFIGSINFO']._serialized_start=1410
  _globals['_PROJECTALERTCONFIGSINFO']._serialized_end=1525
  _globals['_PROJECTALERTCONFIGSTATQUERY']._serialized_start=1527
  _globals['_PROJECTALERTCONFIGSTATQUERY']._serialized_end=1629
  _globals['_PROJECTALERTCONFIG']._serialized_start=1632
  _globals['_PROJECTALERTCONFIG']._serialized_end=2637
# @@protoc_insertion_point(module_scope)
