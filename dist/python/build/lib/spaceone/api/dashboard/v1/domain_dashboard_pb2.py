# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/dashboard/v1/domain_dashboard.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0spaceone/api/dashboard/v1/domain_dashboard.proto\x12\x19spaceone.api.dashboard.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xd1\x03\n\x1c\x43reateDomainDashboardRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12P\n\x07viewers\x18\x02 \x01(\x0e\x32?.spaceone.api.dashboard.v1.CreateDomainDashboardRequest.Viewers\x12+\n\x07layouts\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\tvariables\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08settings\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10variables_schema\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06labels\x18\n \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"4\n\x07Viewers\x12\x10\n\x0cVIEWERS_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02\"\xe6\x02\n\x1cUpdateDomainDashboardRequest\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x07layouts\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\tvariables\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08settings\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10variables_schema\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06labels\x18\n \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"H\n\x16\x44omainDashboardRequest\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"Y\n\x19GetDomainDashboardRequest\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"`\n\x1d\x44omainDashboardVersionRequest\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"q\n GetDomainDashboardVersionRequest\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x11\n\tdomain_id\x18\n \x01(\t\x12\x0c\n\x04only\x18\x0b \x03(\t\"\x8a\x01\n\x1b\x44omainDashboardVersionQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x1b\n\x13\x64omain_dashboard_id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12\x11\n\tdomain_id\x18\n \x01(\t\"\x91\x02\n\x14\x44omainDashboardQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x1b\n\x13\x64omain_dashboard_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12H\n\x07viewers\x18\x04 \x01(\x0e\x32\x37.spaceone.api.dashboard.v1.DomainDashboardQuery.Viewers\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"4\n\x07Viewers\x12\x10\n\x0cVIEWERS_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02\"\xa6\x04\n\x13\x44omainDashboardInfo\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12G\n\x07viewers\x18\x03 \x01(\x0e\x32\x36.spaceone.api.dashboard.v1.DomainDashboardInfo.Viewers\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12+\n\x07layouts\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\tvariables\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08settings\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10variables_schema\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06labels\x18\n \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07user_id\x18\x14 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x16 \x01(\t\x12\x12\n\nupdated_at\x18\x17 \x01(\t\"4\n\x07Viewers\x12\x10\n\x0cVIEWERS_NONE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02\"l\n\x14\x44omainDashboardsInfo\x12?\n\x07results\x18\x01 \x03(\x0b\x32..spaceone.api.dashboard.v1.DomainDashboardInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"c\n\x18\x44omainDashboardStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\xb8\x02\n\x1a\x44omainDashboardVersionInfo\x12\x1b\n\x13\x64omain_dashboard_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x0e\n\x06latest\x18\x03 \x01(\x08\x12+\n\x07layouts\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\tvariables\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08settings\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10variables_schema\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x16 \x01(\t\"z\n\x1b\x44omainDashboardVersionsInfo\x12\x46\n\x07results\x18\x01 \x03(\x0b\x32\x35.spaceone.api.dashboard.v1.DomainDashboardVersionInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xf0\x0c\n\x0f\x44omainDashboard\x12\xa3\x01\n\x06\x63reate\x12\x37.spaceone.api.dashboard.v1.CreateDomainDashboardRequest\x1a..spaceone.api.dashboard.v1.DomainDashboardInfo\"0\x82\xd3\xe4\x93\x02*\"%/dashboard/v1/domain-dashboard/create:\x01*\x12\xa3\x01\n\x06update\x12\x37.spaceone.api.dashboard.v1.UpdateDomainDashboardRequest\x1a..spaceone.api.dashboard.v1.DomainDashboardInfo\"0\x82\xd3\xe4\x93\x02*\"%/dashboard/v1/domain-dashboard/update:\x01*\x12\x85\x01\n\x06\x64\x65lete\x12\x31.spaceone.api.dashboard.v1.DomainDashboardRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02*\"%/dashboard/v1/domain-dashboard/delete:\x01*\x12\x9a\x01\n\x03get\x12\x34.spaceone.api.dashboard.v1.GetDomainDashboardRequest\x1a..spaceone.api.dashboard.v1.DomainDashboardInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/dashboard/v1/domain-dashboard/get:\x01*\x12\x9c\x01\n\x0e\x64\x65lete_version\x12\x38.spaceone.api.dashboard.v1.DomainDashboardVersionRequest\x1a\x16.google.protobuf.Empty\"8\x82\xd3\xe4\x93\x02\x32\"-/dashboard/v1/domain-dashboard/delete-version:\x01*\x12\xb4\x01\n\x0erevert_version\x12\x38.spaceone.api.dashboard.v1.DomainDashboardVersionRequest\x1a..spaceone.api.dashboard.v1.DomainDashboardInfo\"8\x82\xd3\xe4\x93\x02\x32\"-/dashboard/v1/domain-dashboard/revert-version:\x01*\x12\xb8\x01\n\x0bget_version\x12;.spaceone.api.dashboard.v1.GetDomainDashboardVersionRequest\x1a\x35.spaceone.api.dashboard.v1.DomainDashboardVersionInfo\"5\x82\xd3\xe4\x93\x02/\"*/dashboard/v1/domain-dashboard/get-version:\x01*\x12\xb8\x01\n\rlist_versions\x12\x36.spaceone.api.dashboard.v1.DomainDashboardVersionQuery\x1a\x36.spaceone.api.dashboard.v1.DomainDashboardVersionsInfo\"7\x82\xd3\xe4\x93\x02\x31\",/dashboard/v1/domain-dashboard/list-versions:\x01*\x12\x98\x01\n\x04list\x12/.spaceone.api.dashboard.v1.DomainDashboardQuery\x1a/.spaceone.api.dashboard.v1.DomainDashboardsInfo\".\x82\xd3\xe4\x93\x02(\"#/dashboard/v1/domain-dashboard/list:\x01*\x12\x84\x01\n\x04stat\x12\x33.spaceone.api.dashboard.v1.DomainDashboardStatQuery\x1a\x17.google.protobuf.Struct\".\x82\xd3\xe4\x93\x02(\"#/dashboard/v1/domain-dashboard/stat:\x01*B@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/dashboard/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.dashboard.v1.domain_dashboard_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/cloudforet-io/api/dist/go/spaceone/api/dashboard/v1'
  _DOMAINDASHBOARD.methods_by_name['create']._options = None
  _DOMAINDASHBOARD.methods_by_name['create']._serialized_options = b'\202\323\344\223\002*\"%/dashboard/v1/domain-dashboard/create:\001*'
  _DOMAINDASHBOARD.methods_by_name['update']._options = None
  _DOMAINDASHBOARD.methods_by_name['update']._serialized_options = b'\202\323\344\223\002*\"%/dashboard/v1/domain-dashboard/update:\001*'
  _DOMAINDASHBOARD.methods_by_name['delete']._options = None
  _DOMAINDASHBOARD.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002*\"%/dashboard/v1/domain-dashboard/delete:\001*'
  _DOMAINDASHBOARD.methods_by_name['get']._options = None
  _DOMAINDASHBOARD.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\'\"\"/dashboard/v1/domain-dashboard/get:\001*'
  _DOMAINDASHBOARD.methods_by_name['delete_version']._options = None
  _DOMAINDASHBOARD.methods_by_name['delete_version']._serialized_options = b'\202\323\344\223\0022\"-/dashboard/v1/domain-dashboard/delete-version:\001*'
  _DOMAINDASHBOARD.methods_by_name['revert_version']._options = None
  _DOMAINDASHBOARD.methods_by_name['revert_version']._serialized_options = b'\202\323\344\223\0022\"-/dashboard/v1/domain-dashboard/revert-version:\001*'
  _DOMAINDASHBOARD.methods_by_name['get_version']._options = None
  _DOMAINDASHBOARD.methods_by_name['get_version']._serialized_options = b'\202\323\344\223\002/\"*/dashboard/v1/domain-dashboard/get-version:\001*'
  _DOMAINDASHBOARD.methods_by_name['list_versions']._options = None
  _DOMAINDASHBOARD.methods_by_name['list_versions']._serialized_options = b'\202\323\344\223\0021\",/dashboard/v1/domain-dashboard/list-versions:\001*'
  _DOMAINDASHBOARD.methods_by_name['list']._options = None
  _DOMAINDASHBOARD.methods_by_name['list']._serialized_options = b'\202\323\344\223\002(\"#/dashboard/v1/domain-dashboard/list:\001*'
  _DOMAINDASHBOARD.methods_by_name['stat']._options = None
  _DOMAINDASHBOARD.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002(\"#/dashboard/v1/domain-dashboard/stat:\001*'
  _globals['_CREATEDOMAINDASHBOARDREQUEST']._serialized_start=203
  _globals['_CREATEDOMAINDASHBOARDREQUEST']._serialized_end=668
  _globals['_CREATEDOMAINDASHBOARDREQUEST_VIEWERS']._serialized_start=616
  _globals['_CREATEDOMAINDASHBOARDREQUEST_VIEWERS']._serialized_end=668
  _globals['_UPDATEDOMAINDASHBOARDREQUEST']._serialized_start=671
  _globals['_UPDATEDOMAINDASHBOARDREQUEST']._serialized_end=1029
  _globals['_DOMAINDASHBOARDREQUEST']._serialized_start=1031
  _globals['_DOMAINDASHBOARDREQUEST']._serialized_end=1103
  _globals['_GETDOMAINDASHBOARDREQUEST']._serialized_start=1105
  _globals['_GETDOMAINDASHBOARDREQUEST']._serialized_end=1194
  _globals['_DOMAINDASHBOARDVERSIONREQUEST']._serialized_start=1196
  _globals['_DOMAINDASHBOARDVERSIONREQUEST']._serialized_end=1292
  _globals['_GETDOMAINDASHBOARDVERSIONREQUEST']._serialized_start=1294
  _globals['_GETDOMAINDASHBOARDVERSIONREQUEST']._serialized_end=1407
  _globals['_DOMAINDASHBOARDVERSIONQUERY']._serialized_start=1410
  _globals['_DOMAINDASHBOARDVERSIONQUERY']._serialized_end=1548
  _globals['_DOMAINDASHBOARDQUERY']._serialized_start=1551
  _globals['_DOMAINDASHBOARDQUERY']._serialized_end=1824
  _globals['_DOMAINDASHBOARDQUERY_VIEWERS']._serialized_start=616
  _globals['_DOMAINDASHBOARDQUERY_VIEWERS']._serialized_end=668
  _globals['_DOMAINDASHBOARDINFO']._serialized_start=1827
  _globals['_DOMAINDASHBOARDINFO']._serialized_end=2377
  _globals['_DOMAINDASHBOARDINFO_VIEWERS']._serialized_start=616
  _globals['_DOMAINDASHBOARDINFO_VIEWERS']._serialized_end=668
  _globals['_DOMAINDASHBOARDSINFO']._serialized_start=2379
  _globals['_DOMAINDASHBOARDSINFO']._serialized_end=2487
  _globals['_DOMAINDASHBOARDSTATQUERY']._serialized_start=2489
  _globals['_DOMAINDASHBOARDSTATQUERY']._serialized_end=2588
  _globals['_DOMAINDASHBOARDVERSIONINFO']._serialized_start=2591
  _globals['_DOMAINDASHBOARDVERSIONINFO']._serialized_end=2903
  _globals['_DOMAINDASHBOARDVERSIONSINFO']._serialized_start=2905
  _globals['_DOMAINDASHBOARDVERSIONSINFO']._serialized_end=3027
  _globals['_DOMAINDASHBOARD']._serialized_start=3030
  _globals['_DOMAINDASHBOARD']._serialized_end=4678
# @@protoc_insertion_point(module_scope)
