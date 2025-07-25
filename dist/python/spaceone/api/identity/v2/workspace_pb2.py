# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v2/workspace.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(spaceone/api/identity/v2/workspace.proto\x12\x18spaceone.api.identity.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"/\n\x11WorkspaceCostInfo\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x02\x12\r\n\x05month\x18\x02 \x01(\x02\"M\n\x16\x43reateWorkSpaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04tags\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"c\n\x16UpdateWorkSpaceRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"O\n\x1b\x43hangeWorkspaceGroupRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x1a\n\x12workspace_group_id\x18\x02 \x01(\t\"=\n\x16WorkspaceDeleteRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"C\n\x17WorkspacePackageRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\t\"(\n\x10WorkspaceRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\"@\n\x15WorkspaceCheckRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xd7\x04\n\rWorkspaceInfo\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x05state\x18\x03 \x01(\x0e\x32-.spaceone.api.identity.v2.WorkspaceInfo.State\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ncreated_by\x18\x05 \x01(\t\x12\x12\n\nreferences\x18\x06 \x03(\t\x12\x12\n\nis_managed\x18\x07 \x01(\x08\x12\x10\n\x08packages\x18\x08 \x03(\t\x12\x12\n\nis_dormant\x18\x0b \x01(\x08\x12\x13\n\x0b\x64ormant_ttl\x18\x0c \x01(\x05\x12\x1d\n\x15service_account_count\x18\r \x01(\x05\x12\x12\n\nuser_count\x18\x0e \x01(\x05\x12>\n\tcost_info\x18\x0f \x01(\x0b\x32+.spaceone.api.identity.v2.WorkspaceCostInfo\x12\x1a\n\x12workspace_group_id\x18\x15 \x01(\t\x12\x11\n\tdomain_id\x18\x16 \x01(\t\x12\x1a\n\x12trusted_account_id\x18\x17 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x16\n\x0elast_synced_at\x18  \x01(\t\x12\x1a\n\x12\x64ormant_updated_at\x18! \x01(\t\x12\x12\n\nchanged_at\x18\" \x01(\t\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xb1\x02\n\x14WorkspaceSearchQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x14\n\x0cworkspace_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x43\n\x05state\x18\x04 \x01(\x0e\x32\x34.spaceone.api.identity.v2.WorkspaceSearchQuery.State\x12\x12\n\ncreated_by\x18\x05 \x01(\t\x12\x12\n\nis_managed\x18\x06 \x01(\x08\x12\x12\n\nis_dormant\x18\x07 \x01(\x08\x12\x1a\n\x12workspace_group_id\x18\x08 \x01(\t\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"_\n\x0eWorkspacesInfo\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\'.spaceone.api.identity.v2.WorkspaceInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"J\n\x15WorkspaceAnalyzeQuery\x12\x31\n\x05query\x18\x01 \x01(\x0b\x32\".spaceone.api.core.v2.AnalyzeQuery\"J\n\x12WorkspaceStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\x8a\x0e\n\tWorkspace\x12\x8d\x01\n\x06\x63reate\x12\x30.spaceone.api.identity.v2.CreateWorkSpaceRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"(\x82\xd3\xe4\x93\x02\"\"\x1d/identity/v2/workspace/create:\x01*\x12\x8d\x01\n\x06update\x12\x30.spaceone.api.identity.v2.UpdateWorkSpaceRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"(\x82\xd3\xe4\x93\x02\"\"\x1d/identity/v2/workspace/update:\x01*\x12\xb2\x01\n\x16\x63hange_workspace_group\x12\x35.spaceone.api.identity.v2.ChangeWorkspaceGroupRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"8\x82\xd3\xe4\x93\x02\x32\"-/identity/v2/workspace/change-workspace-group:\x01*\x12|\n\x06\x64\x65lete\x12\x30.spaceone.api.identity.v2.WorkspaceDeleteRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\"\x1d/identity/v2/workspace/delete:\x01*\x12\x87\x01\n\x06\x65nable\x12*.spaceone.api.identity.v2.WorkspaceRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"(\x82\xd3\xe4\x93\x02\"\"\x1d/identity/v2/workspace/enable:\x01*\x12\x89\x01\n\x07\x64isable\x12*.spaceone.api.identity.v2.WorkspaceRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/identity/v2/workspace/disable:\x01*\x12\x98\x01\n\x0b\x61\x64\x64_package\x12\x31.spaceone.api.identity.v2.WorkspacePackageRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"-\x82\xd3\xe4\x93\x02\'\"\"/identity/v2/workspace/add-package:\x01*\x12\x9e\x01\n\x0eremove_package\x12\x31.spaceone.api.identity.v2.WorkspacePackageRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"0\x82\xd3\xe4\x93\x02*\"%/identity/v2/workspace/remove-package:\x01*\x12\x81\x01\n\x03get\x12*.spaceone.api.identity.v2.WorkspaceRequest\x1a\'.spaceone.api.identity.v2.WorkspaceInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/identity/v2/workspace/get:\x01*\x12R\n\x05\x63heck\x12/.spaceone.api.identity.v2.WorkspaceCheckRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x88\x01\n\x04list\x12..spaceone.api.identity.v2.WorkspaceSearchQuery\x1a(.spaceone.api.identity.v2.WorkspacesInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/identity/v2/workspace/list:\x01*\x12~\n\x07\x61nalyze\x12/.spaceone.api.identity.v2.WorkspaceAnalyzeQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"\x1e/identity/v2/workspace/analyze:\x01*\x12u\n\x04stat\x12,.spaceone.api.identity.v2.WorkspaceStatQuery\x1a\x17.google.protobuf.Struct\"&\x82\xd3\xe4\x93\x02 \"\x1b/identity/v2/workspace/stat:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v2.workspace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2'
  _globals['_WORKSPACE'].methods_by_name['create']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002\"\"\035/identity/v2/workspace/create:\001*'
  _globals['_WORKSPACE'].methods_by_name['update']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002\"\"\035/identity/v2/workspace/update:\001*'
  _globals['_WORKSPACE'].methods_by_name['change_workspace_group']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['change_workspace_group']._serialized_options = b'\202\323\344\223\0022\"-/identity/v2/workspace/change-workspace-group:\001*'
  _globals['_WORKSPACE'].methods_by_name['delete']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\"\"\035/identity/v2/workspace/delete:\001*'
  _globals['_WORKSPACE'].methods_by_name['enable']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['enable']._serialized_options = b'\202\323\344\223\002\"\"\035/identity/v2/workspace/enable:\001*'
  _globals['_WORKSPACE'].methods_by_name['disable']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['disable']._serialized_options = b'\202\323\344\223\002#\"\036/identity/v2/workspace/disable:\001*'
  _globals['_WORKSPACE'].methods_by_name['add_package']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['add_package']._serialized_options = b'\202\323\344\223\002\'\"\"/identity/v2/workspace/add-package:\001*'
  _globals['_WORKSPACE'].methods_by_name['remove_package']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['remove_package']._serialized_options = b'\202\323\344\223\002*\"%/identity/v2/workspace/remove-package:\001*'
  _globals['_WORKSPACE'].methods_by_name['get']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002\037\"\032/identity/v2/workspace/get:\001*'
  _globals['_WORKSPACE'].methods_by_name['list']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002 \"\033/identity/v2/workspace/list:\001*'
  _globals['_WORKSPACE'].methods_by_name['analyze']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002#\"\036/identity/v2/workspace/analyze:\001*'
  _globals['_WORKSPACE'].methods_by_name['stat']._loaded_options = None
  _globals['_WORKSPACE'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002 \"\033/identity/v2/workspace/stat:\001*'
  _globals['_WORKSPACECOSTINFO']._serialized_start=193
  _globals['_WORKSPACECOSTINFO']._serialized_end=240
  _globals['_CREATEWORKSPACEREQUEST']._serialized_start=242
  _globals['_CREATEWORKSPACEREQUEST']._serialized_end=319
  _globals['_UPDATEWORKSPACEREQUEST']._serialized_start=321
  _globals['_UPDATEWORKSPACEREQUEST']._serialized_end=420
  _globals['_CHANGEWORKSPACEGROUPREQUEST']._serialized_start=422
  _globals['_CHANGEWORKSPACEGROUPREQUEST']._serialized_end=501
  _globals['_WORKSPACEDELETEREQUEST']._serialized_start=503
  _globals['_WORKSPACEDELETEREQUEST']._serialized_end=564
  _globals['_WORKSPACEPACKAGEREQUEST']._serialized_start=566
  _globals['_WORKSPACEPACKAGEREQUEST']._serialized_end=633
  _globals['_WORKSPACEREQUEST']._serialized_start=635
  _globals['_WORKSPACEREQUEST']._serialized_end=675
  _globals['_WORKSPACECHECKREQUEST']._serialized_start=677
  _globals['_WORKSPACECHECKREQUEST']._serialized_end=741
  _globals['_WORKSPACEINFO']._serialized_start=744
  _globals['_WORKSPACEINFO']._serialized_end=1343
  _globals['_WORKSPACEINFO_STATE']._serialized_start=1299
  _globals['_WORKSPACEINFO_STATE']._serialized_end=1343
  _globals['_WORKSPACESEARCHQUERY']._serialized_start=1346
  _globals['_WORKSPACESEARCHQUERY']._serialized_end=1651
  _globals['_WORKSPACESEARCHQUERY_STATE']._serialized_start=1299
  _globals['_WORKSPACESEARCHQUERY_STATE']._serialized_end=1343
  _globals['_WORKSPACESINFO']._serialized_start=1653
  _globals['_WORKSPACESINFO']._serialized_end=1748
  _globals['_WORKSPACEANALYZEQUERY']._serialized_start=1750
  _globals['_WORKSPACEANALYZEQUERY']._serialized_end=1824
  _globals['_WORKSPACESTATQUERY']._serialized_start=1826
  _globals['_WORKSPACESTATQUERY']._serialized_end=1900
  _globals['_WORKSPACE']._serialized_start=1903
  _globals['_WORKSPACE']._serialized_end=3705
# @@protoc_insertion_point(module_scope)
