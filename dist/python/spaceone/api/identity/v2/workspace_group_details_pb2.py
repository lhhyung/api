# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v2/workspace_group_details.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6spaceone/api/identity/v2/workspace_group_details.proto\x12\x18spaceone.api.identity.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"u\n\"UpdateWorkspaceGroupDetailsRequest\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"X\n&WorkspacesWorkspaceGroupDetailsRequest\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\x12\x12\n\nworkspaces\x18\x02 \x03(\t\"\x85\x02\n WorkspaceGroupDetailsFindRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12O\n\x05state\x18\x02 \x01(\x0e\x32@.spaceone.api.identity.v2.WorkspaceGroupDetailsFindRequest.State\x12(\n\x04page\x18\x03 \x01(\x0b\x32\x1a.spaceone.api.core.v2.Page\x12\x1a\n\x12workspace_group_id\x18\x15 \x01(\t\"9\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x0b\n\x07PENDING\x10\x03\"P\n\x19WorkspaceGroupDetailsUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\t\x12\x11\n\trole_type\x18\x03 \x01(\t\"\x86\x01\n$AddUsersWorkspaceGroupDetailsRequest\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\x12\x42\n\x05users\x18\x02 \x03(\x0b\x32\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsUser\"T\n\'RemoveUsersWorkspaceGroupDetailsRequest\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\x12\r\n\x05users\x18\x02 \x03(\t\"@\n\"DeleteWorkspaceGroupDetailsRequest\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\"\x1e\n\x1cWorkspaceGroupDetailsRequest\"\xf2\x01\n\x19WorkspaceGroupDetailsInfo\x12\x1a\n\x12workspace_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nworkspaces\x18\x03 \x03(\t\x12\r\n\x05users\x18\x04 \x03(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12\x12\n\nupdated_by\x18\x07 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"\xdb\x01\n$WorkspaceGroupDetailsUserSummaryInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12S\n\x05state\x18\x03 \x01(\x0e\x32\x44.spaceone.api.identity.v2.WorkspaceGroupDetailsUserSummaryInfo.State\"?\n\x05State\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x12\x0b\n\x07PENDING\x10\x03\"\x8d\x01\n%WorkspaceGroupDetailsUsersSummaryInfo\x12O\n\x07results\x18\x01 \x03(\x0b\x32>.spaceone.api.identity.v2.WorkspaceGroupDetailsUserSummaryInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"w\n\x1aWorkspaceGroupsDetailsInfo\x12\x44\n\x07results\x18\x01 \x03(\x0b\x32\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\x9a\x0c\n\x15WorkspaceGroupDetails\x12\xb3\x01\n\x06update\x12<.spaceone.api.identity.v2.UpdateWorkspaceGroupDetailsRequest\x1a\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\"6\x82\xd3\xe4\x93\x02\x30\"+/identity/v2/workspace-group-details/update:\x01*\x12\x96\x01\n\x06\x64\x65lete\x12<.spaceone.api.identity.v2.DeleteWorkspaceGroupDetailsRequest\x1a\x16.google.protobuf.Empty\"6\x82\xd3\xe4\x93\x02\x30\"+/identity/v2/workspace-group-details/delete:\x01*\x12\xc7\x01\n\x0e\x61\x64\x64_workspaces\x12@.spaceone.api.identity.v2.WorkspacesWorkspaceGroupDetailsRequest\x1a\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\">\x82\xd3\xe4\x93\x02\x38\"3/identity/v2/workspace-group-details/add-workspaces:\x01*\x12\xcd\x01\n\x11remove_workspaces\x12@.spaceone.api.identity.v2.WorkspacesWorkspaceGroupDetailsRequest\x1a\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\"A\x82\xd3\xe4\x93\x02;\"6/identity/v2/workspace-group-details/remove-workspaces:\x01*\x12\xc5\x01\n\nfind_users\x12:.spaceone.api.identity.v2.WorkspaceGroupDetailsFindRequest\x1a?.spaceone.api.identity.v2.WorkspaceGroupDetailsUsersSummaryInfo\":\x82\xd3\xe4\x93\x02\x34\"//identity/v2/workspace-group-details/find-users:\x01*\x12\xbb\x01\n\tadd_users\x12>.spaceone.api.identity.v2.AddUsersWorkspaceGroupDetailsRequest\x1a\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\"9\x82\xd3\xe4\x93\x02\x33\"./identity/v2/workspace-group-details/add-users:\x01*\x12\xc4\x01\n\x0cremove_users\x12\x41.spaceone.api.identity.v2.RemoveUsersWorkspaceGroupDetailsRequest\x1a\x33.spaceone.api.identity.v2.WorkspaceGroupDetailsInfo\"<\x82\xd3\xe4\x93\x02\x36\"1/identity/v2/workspace-group-details/remove-users:\x01*\x12\xca\x01\n\x14get_workspace_groups\x12\x36.spaceone.api.identity.v2.WorkspaceGroupDetailsRequest\x1a\x34.spaceone.api.identity.v2.WorkspaceGroupsDetailsInfo\"D\x82\xd3\xe4\x93\x02>\"9/identity/v2/workspace-group-details/get-workspace-groups:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v2.workspace_group_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['update']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['update']._serialized_options = b'\202\323\344\223\0020\"+/identity/v2/workspace-group-details/update:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['delete']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\0020\"+/identity/v2/workspace-group-details/delete:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['add_workspaces']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['add_workspaces']._serialized_options = b'\202\323\344\223\0028\"3/identity/v2/workspace-group-details/add-workspaces:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['remove_workspaces']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['remove_workspaces']._serialized_options = b'\202\323\344\223\002;\"6/identity/v2/workspace-group-details/remove-workspaces:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['find_users']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['find_users']._serialized_options = b'\202\323\344\223\0024\"//identity/v2/workspace-group-details/find-users:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['add_users']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['add_users']._serialized_options = b'\202\323\344\223\0023\"./identity/v2/workspace-group-details/add-users:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['remove_users']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['remove_users']._serialized_options = b'\202\323\344\223\0026\"1/identity/v2/workspace-group-details/remove-users:\001*'
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['get_workspace_groups']._loaded_options = None
  _globals['_WORKSPACEGROUPDETAILS'].methods_by_name['get_workspace_groups']._serialized_options = b'\202\323\344\223\002>\"9/identity/v2/workspace-group-details/get-workspace-groups:\001*'
  _globals['_UPDATEWORKSPACEGROUPDETAILSREQUEST']._serialized_start=207
  _globals['_UPDATEWORKSPACEGROUPDETAILSREQUEST']._serialized_end=324
  _globals['_WORKSPACESWORKSPACEGROUPDETAILSREQUEST']._serialized_start=326
  _globals['_WORKSPACESWORKSPACEGROUPDETAILSREQUEST']._serialized_end=414
  _globals['_WORKSPACEGROUPDETAILSFINDREQUEST']._serialized_start=417
  _globals['_WORKSPACEGROUPDETAILSFINDREQUEST']._serialized_end=678
  _globals['_WORKSPACEGROUPDETAILSFINDREQUEST_STATE']._serialized_start=621
  _globals['_WORKSPACEGROUPDETAILSFINDREQUEST_STATE']._serialized_end=678
  _globals['_WORKSPACEGROUPDETAILSUSER']._serialized_start=680
  _globals['_WORKSPACEGROUPDETAILSUSER']._serialized_end=760
  _globals['_ADDUSERSWORKSPACEGROUPDETAILSREQUEST']._serialized_start=763
  _globals['_ADDUSERSWORKSPACEGROUPDETAILSREQUEST']._serialized_end=897
  _globals['_REMOVEUSERSWORKSPACEGROUPDETAILSREQUEST']._serialized_start=899
  _globals['_REMOVEUSERSWORKSPACEGROUPDETAILSREQUEST']._serialized_end=983
  _globals['_DELETEWORKSPACEGROUPDETAILSREQUEST']._serialized_start=985
  _globals['_DELETEWORKSPACEGROUPDETAILSREQUEST']._serialized_end=1049
  _globals['_WORKSPACEGROUPDETAILSREQUEST']._serialized_start=1051
  _globals['_WORKSPACEGROUPDETAILSREQUEST']._serialized_end=1081
  _globals['_WORKSPACEGROUPDETAILSINFO']._serialized_start=1084
  _globals['_WORKSPACEGROUPDETAILSINFO']._serialized_end=1326
  _globals['_WORKSPACEGROUPDETAILSUSERSUMMARYINFO']._serialized_start=1329
  _globals['_WORKSPACEGROUPDETAILSUSERSUMMARYINFO']._serialized_end=1548
  _globals['_WORKSPACEGROUPDETAILSUSERSUMMARYINFO_STATE']._serialized_start=1485
  _globals['_WORKSPACEGROUPDETAILSUSERSUMMARYINFO_STATE']._serialized_end=1548
  _globals['_WORKSPACEGROUPDETAILSUSERSSUMMARYINFO']._serialized_start=1551
  _globals['_WORKSPACEGROUPDETAILSUSERSSUMMARYINFO']._serialized_end=1692
  _globals['_WORKSPACEGROUPSDETAILSINFO']._serialized_start=1694
  _globals['_WORKSPACEGROUPSDETAILSINFO']._serialized_end=1813
  _globals['_WORKSPACEGROUPDETAILS']._serialized_start=1816
  _globals['_WORKSPACEGROUPDETAILS']._serialized_end=3378
# @@protoc_insertion_point(module_scope)
