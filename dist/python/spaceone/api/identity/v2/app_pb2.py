# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v2/app.proto
# Protobuf Python Version: 5.26.1
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
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"spaceone/api/identity/v2/app.proto\x12\x18spaceone.api.identity.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xc5\x02\n\x10\x43reateAppRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nexpired_at\x18\x04 \x01(\t\x12P\n\x0eresource_group\x18\x14 \x01(\x0e\x32\x38.spaceone.api.identity.v2.CreateAppRequest.ResourceGroup\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x18\n\x10project_group_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\"A\n\rResourceGroup\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\x12\x0b\n\x07PROJECT\x10\x03\"W\n\x10UpdateAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\">\n\x18GenerateAPIKeyAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x12\n\nexpired_at\x18\x02 \x01(\t\"\x1c\n\nAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"7\n\x0f\x41ppCheckRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"5\n\x0c\x43heckAppInfo\x12\x13\n\x0bpermissions\x18\x01 \x03(\t\x12\x10\n\x08projects\x18\x02 \x03(\t\"\xdd\x05\n\x07\x41ppInfo\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x15\n\rclient_secret\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x36\n\x05state\x18\x04 \x01(\x0e\x32\'.spaceone.api.identity.v2.AppInfo.State\x12\x12\n\nis_managed\x18\x05 \x01(\x08\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12=\n\trole_type\x18\x07 \x01(\x0e\x32*.spaceone.api.identity.v2.AppInfo.RoleType\x12G\n\x0eresource_group\x18\x14 \x01(\x0e\x32/.spaceone.api.identity.v2.AppInfo.ResourceGroup\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x0f\n\x07role_id\x18\x17 \x01(\t\x12\x11\n\tclient_id\x18\x18 \x01(\t\x12\x18\n\x10project_group_id\x18\x19 \x01(\t\x12\x12\n\nproject_id\x18\x1a \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nexpired_at\x18  \x01(\t\x12\x18\n\x10last_accessed_at\x18! \x01(\t\"?\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\"[\n\x08RoleType\x12\x12\n\x0eROLE_TYPE_NONE\x10\x00\x12\x10\n\x0c\x44OMAIN_ADMIN\x10\x01\x12\x13\n\x0fWORKSPACE_OWNER\x10\x02\x12\x14\n\x10WORKSPACE_MEMBER\x10\x03\"G\n\rResourceGroup\x12\x0e\n\nGROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\x12\x0b\n\x07PROJECT\x10\x03\"\xdd\x03\n\x0e\x41ppSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12=\n\x05state\x18\x04 \x01(\x0e\x32..spaceone.api.identity.v2.AppSearchQuery.State\x12\x44\n\trole_type\x18\x05 \x01(\x0e\x32\x31.spaceone.api.identity.v2.AppSearchQuery.RoleType\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x0f\n\x07role_id\x18\x16 \x01(\t\x12\x11\n\tclient_id\x18\x17 \x01(\t\"?\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\"E\n\x08RoleType\x12\x12\n\x0eROLE_TYPE_NONE\x10\x00\x12\x10\n\x0c\x44OMAIN_ADMIN\x10\x01\x12\x13\n\x0fWORKSPACE_OWNER\x10\x02\":\n\rResourceGroup\x12\x0e\n\nGROUP_NONE\x10\x00\x12\n\n\x06\x44OMAIN\x10\x01\x12\r\n\tWORKSPACE\x10\x02\"S\n\x08\x41ppsInfo\x12\x32\n\x07results\x18\x01 \x03(\x0b\x32!.spaceone.api.identity.v2.AppInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"D\n\x0c\x41ppStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xb3\t\n\x03\x41pp\x12{\n\x06\x63reate\x12*.spaceone.api.identity.v2.CreateAppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v2/app/create:\x01*\x12{\n\x06update\x12*.spaceone.api.identity.v2.UpdateAppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v2/app/update:\x01*\x12\xa3\x01\n\x16generate_client_secret\x12\x32.spaceone.api.identity.v2.GenerateAPIKeyAppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"2\x82\xd3\xe4\x93\x02,\"\'/identity/v2/app/generate-client-secret:\x01*\x12u\n\x06\x65nable\x12$.spaceone.api.identity.v2.AppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v2/app/enable:\x01*\x12w\n\x07\x64isable\x12$.spaceone.api.identity.v2.AppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v2/app/disable:\x01*\x12j\n\x06\x64\x65lete\x12$.spaceone.api.identity.v2.AppRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v2/app/delete:\x01*\x12o\n\x03get\x12$.spaceone.api.identity.v2.AppRequest\x1a!.spaceone.api.identity.v2.AppInfo\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/identity/v2/app/get:\x01*\x12\\\n\x05\x63heck\x12).spaceone.api.identity.v2.AppCheckRequest\x1a&.spaceone.api.identity.v2.CheckAppInfo\"\x00\x12v\n\x04list\x12(.spaceone.api.identity.v2.AppSearchQuery\x1a\".spaceone.api.identity.v2.AppsInfo\" \x82\xd3\xe4\x93\x02\x1a\"\x15/identity/v2/app/list:\x01*\x12i\n\x04stat\x12&.spaceone.api.identity.v2.AppStatQuery\x1a\x17.google.protobuf.Struct\" \x82\xd3\xe4\x93\x02\x1a\"\x15/identity/v2/app/stat:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v2.app_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2'
  _globals['_APP'].methods_by_name['create']._loaded_options = None
  _globals['_APP'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v2/app/create:\001*'
  _globals['_APP'].methods_by_name['update']._loaded_options = None
  _globals['_APP'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v2/app/update:\001*'
  _globals['_APP'].methods_by_name['generate_client_secret']._loaded_options = None
  _globals['_APP'].methods_by_name['generate_client_secret']._serialized_options = b'\202\323\344\223\002,\"\'/identity/v2/app/generate-client-secret:\001*'
  _globals['_APP'].methods_by_name['enable']._loaded_options = None
  _globals['_APP'].methods_by_name['enable']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v2/app/enable:\001*'
  _globals['_APP'].methods_by_name['disable']._loaded_options = None
  _globals['_APP'].methods_by_name['disable']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v2/app/disable:\001*'
  _globals['_APP'].methods_by_name['delete']._loaded_options = None
  _globals['_APP'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v2/app/delete:\001*'
  _globals['_APP'].methods_by_name['get']._loaded_options = None
  _globals['_APP'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\031\"\024/identity/v2/app/get:\001*'
  _globals['_APP'].methods_by_name['list']._loaded_options = None
  _globals['_APP'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002\032\"\025/identity/v2/app/list:\001*'
  _globals['_APP'].methods_by_name['stat']._loaded_options = None
  _globals['_APP'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\032\"\025/identity/v2/app/stat:\001*'
  _globals['_CREATEAPPREQUEST']._serialized_start=188
  _globals['_CREATEAPPREQUEST']._serialized_end=513
  _globals['_CREATEAPPREQUEST_RESOURCEGROUP']._serialized_start=448
  _globals['_CREATEAPPREQUEST_RESOURCEGROUP']._serialized_end=513
  _globals['_UPDATEAPPREQUEST']._serialized_start=515
  _globals['_UPDATEAPPREQUEST']._serialized_end=602
  _globals['_GENERATEAPIKEYAPPREQUEST']._serialized_start=604
  _globals['_GENERATEAPIKEYAPPREQUEST']._serialized_end=666
  _globals['_APPREQUEST']._serialized_start=668
  _globals['_APPREQUEST']._serialized_end=696
  _globals['_APPCHECKREQUEST']._serialized_start=698
  _globals['_APPCHECKREQUEST']._serialized_end=753
  _globals['_CHECKAPPINFO']._serialized_start=755
  _globals['_CHECKAPPINFO']._serialized_end=808
  _globals['_APPINFO']._serialized_start=811
  _globals['_APPINFO']._serialized_end=1544
  _globals['_APPINFO_STATE']._serialized_start=1315
  _globals['_APPINFO_STATE']._serialized_end=1378
  _globals['_APPINFO_ROLETYPE']._serialized_start=1380
  _globals['_APPINFO_ROLETYPE']._serialized_end=1471
  _globals['_APPINFO_RESOURCEGROUP']._serialized_start=1473
  _globals['_APPINFO_RESOURCEGROUP']._serialized_end=1544
  _globals['_APPSEARCHQUERY']._serialized_start=1547
  _globals['_APPSEARCHQUERY']._serialized_end=2024
  _globals['_APPSEARCHQUERY_STATE']._serialized_start=1315
  _globals['_APPSEARCHQUERY_STATE']._serialized_end=1378
  _globals['_APPSEARCHQUERY_ROLETYPE']._serialized_start=1380
  _globals['_APPSEARCHQUERY_ROLETYPE']._serialized_end=1449
  _globals['_APPSEARCHQUERY_RESOURCEGROUP']._serialized_start=1473
  _globals['_APPSEARCHQUERY_RESOURCEGROUP']._serialized_end=1531
  _globals['_APPSINFO']._serialized_start=2026
  _globals['_APPSINFO']._serialized_end=2109
  _globals['_APPSTATQUERY']._serialized_start=2111
  _globals['_APPSTATQUERY']._serialized_end=2179
  _globals['_APP']._serialized_start=2182
  _globals['_APP']._serialized_end=3385
# @@protoc_insertion_point(module_scope)
