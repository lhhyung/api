# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory_v2/v1/namespace_group.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2spaceone/api/inventory_v2/v1/namespace_group.proto\x12\x1cspaceone.api.inventory_v2.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xbf\x01\n\x1b\x43reateNamespaceGroupRequest\x12\x1a\n\x12namespace_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x16\n\x0eresource_group\x18\x14 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\"\x91\x01\n\x1bUpdateNamespaceGroupRequest\x12\x1a\n\x12namespace_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"3\n\x15NamespaceGroupRequest\x12\x1a\n\x12namespace_group_id\x18\x01 \x01(\t\"\x87\x01\n\x13NamespaceGroupQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x1a\n\x12namespace_group_id\x18\x02 \x01(\t\x12\x12\n\nexist_only\x18\x03 \x01(\x08\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\"\x85\x02\n\x12NamespaceGroupInfo\x12\x1a\n\x12namespace_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nis_managed\x18\x06 \x01(\x08\x12\x16\n\x0eresource_group\x18\x14 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\x12\x12\n\nupdated_at\x18  \x01(\t\"m\n\x13NamespaceGroupsInfo\x12\x41\n\x07results\x18\x01 \x03(\x0b\x32\x30.spaceone.api.inventory_v2.v1.NamespaceGroupInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"O\n\x17NamespaceGroupStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery2\xc0\x07\n\x0eNamespaceGroup\x12\xa9\x01\n\x06\x63reate\x12\x39.spaceone.api.inventory_v2.v1.CreateNamespaceGroupRequest\x1a\x30.spaceone.api.inventory_v2.v1.NamespaceGroupInfo\"2\x82\xd3\xe4\x93\x02,\"\'/inventory-v2/v1/namespace-group/create:\x01*\x12\xa9\x01\n\x06update\x12\x39.spaceone.api.inventory_v2.v1.UpdateNamespaceGroupRequest\x1a\x30.spaceone.api.inventory_v2.v1.NamespaceGroupInfo\"2\x82\xd3\xe4\x93\x02,\"\'/inventory-v2/v1/namespace-group/update:\x01*\x12\x89\x01\n\x06\x64\x65lete\x12\x33.spaceone.api.inventory_v2.v1.NamespaceGroupRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/inventory-v2/v1/namespace-group/delete:\x01*\x12\x9d\x01\n\x03get\x12\x33.spaceone.api.inventory_v2.v1.NamespaceGroupRequest\x1a\x30.spaceone.api.inventory_v2.v1.NamespaceGroupInfo\"/\x82\xd3\xe4\x93\x02)\"$/inventory-v2/v1/namespace-group/get:\x01*\x12\x9e\x01\n\x04list\x12\x31.spaceone.api.inventory_v2.v1.NamespaceGroupQuery\x1a\x31.spaceone.api.inventory_v2.v1.NamespaceGroupsInfo\"0\x82\xd3\xe4\x93\x02*\"%/inventory-v2/v1/namespace-group/list:\x01*\x12\x88\x01\n\x04stat\x12\x35.spaceone.api.inventory_v2.v1.NamespaceGroupStatQuery\x1a\x17.google.protobuf.Struct\"0\x82\xd3\xe4\x93\x02*\"%/inventory-v2/v1/namespace-group/stat:\x01*BCZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory-v2/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.inventory_v2.v1.namespace_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/inventory-v2/v1'
  _globals['_NAMESPACEGROUP'].methods_by_name['create']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002,\"\'/inventory-v2/v1/namespace-group/create:\001*'
  _globals['_NAMESPACEGROUP'].methods_by_name['update']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002,\"\'/inventory-v2/v1/namespace-group/update:\001*'
  _globals['_NAMESPACEGROUP'].methods_by_name['delete']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002,\"\'/inventory-v2/v1/namespace-group/delete:\001*'
  _globals['_NAMESPACEGROUP'].methods_by_name['get']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002)\"$/inventory-v2/v1/namespace-group/get:\001*'
  _globals['_NAMESPACEGROUP'].methods_by_name['list']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002*\"%/inventory-v2/v1/namespace-group/list:\001*'
  _globals['_NAMESPACEGROUP'].methods_by_name['stat']._loaded_options = None
  _globals['_NAMESPACEGROUP'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002*\"%/inventory-v2/v1/namespace-group/stat:\001*'
  _globals['_CREATENAMESPACEGROUPREQUEST']._serialized_start=208
  _globals['_CREATENAMESPACEGROUPREQUEST']._serialized_end=399
  _globals['_UPDATENAMESPACEGROUPREQUEST']._serialized_start=402
  _globals['_UPDATENAMESPACEGROUPREQUEST']._serialized_end=547
  _globals['_NAMESPACEGROUPREQUEST']._serialized_start=549
  _globals['_NAMESPACEGROUPREQUEST']._serialized_end=600
  _globals['_NAMESPACEGROUPQUERY']._serialized_start=603
  _globals['_NAMESPACEGROUPQUERY']._serialized_end=738
  _globals['_NAMESPACEGROUPINFO']._serialized_start=741
  _globals['_NAMESPACEGROUPINFO']._serialized_end=1002
  _globals['_NAMESPACEGROUPSINFO']._serialized_start=1004
  _globals['_NAMESPACEGROUPSINFO']._serialized_end=1113
  _globals['_NAMESPACEGROUPSTATQUERY']._serialized_start=1115
  _globals['_NAMESPACEGROUPSTATQUERY']._serialized_end=1194
  _globals['_NAMESPACEGROUP']._serialized_start=1197
  _globals['_NAMESPACEGROUP']._serialized_end=2157
# @@protoc_insertion_point(module_scope)