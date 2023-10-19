# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/secret/v1/trusted_secret.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+spaceone/api/secret/v1/trusted_secret.proto\x12\x16spaceone.api.secret.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xb7\x01\n\x1a\x43reateTrustedSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x1a\n\x12service_account_id\x18\x05 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\x7f\n\x1aUpdateTrustedSecretRequest\x12\x19\n\x11trusted_secret_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"D\n\x14TrustedSecretRequest\x12\x19\n\x11trusted_secret_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\x85\x01\n\x1eUpdateTrustedSecretDataRequest\x12\x19\n\x11trusted_secret_id\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"U\n\x17GetTrustedSecretRequest\x12\x19\n\x11trusted_secret_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xba\x01\n\x12TrustedSecretQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x19\n\x11trusted_secret_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x06 \x01(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x1a\n\x12service_account_id\x18\t \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xdc\x01\n\x11TrustedSecretInfo\x12\x19\n\x11trusted_secret_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\x1a\n\x12service_account_id\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x16 \x01(\t\"e\n\x12TrustedSecretsInfo\x12:\n\x07results\x18\x01 \x03(\x0b\x32).spaceone.api.secret.v1.TrustedSecretInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"a\n\x16TrustedSecretStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xe2\x07\n\rTrustedSecret\x12\x94\x01\n\x06\x63reate\x12\x32.spaceone.api.secret.v1.CreateTrustedSecretRequest\x1a).spaceone.api.secret.v1.TrustedSecretInfo\"+\x82\xd3\xe4\x93\x02%\" /secret/v1/trusted-secret/create:\x01*\x12\x94\x01\n\x06update\x12\x32.spaceone.api.secret.v1.UpdateTrustedSecretRequest\x1a).spaceone.api.secret.v1.TrustedSecretInfo\"+\x82\xd3\xe4\x93\x02%\" /secret/v1/trusted-secret/update:\x01*\x12{\n\x06\x64\x65lete\x12,.spaceone.api.secret.v1.TrustedSecretRequest\x1a\x16.google.protobuf.Empty\"+\x82\xd3\xe4\x93\x02%\" /secret/v1/trusted-secret/delete:\x01*\x12\x8f\x01\n\x0bupdate_data\x12\x36.spaceone.api.secret.v1.UpdateTrustedSecretDataRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02*\"%/secret/v1/trusted-secret/update-data:\x01*\x12\x8b\x01\n\x03get\x12/.spaceone.api.secret.v1.GetTrustedSecretRequest\x1a).spaceone.api.secret.v1.TrustedSecretInfo\"(\x82\xd3\xe4\x93\x02\"\"\x1d/secret/v1/trusted-secret/get:\x01*\x12\x89\x01\n\x04list\x12*.spaceone.api.secret.v1.TrustedSecretQuery\x1a*.spaceone.api.secret.v1.TrustedSecretsInfo\")\x82\xd3\xe4\x93\x02#\"\x1e/secret/v1/trusted-secret/list:\x01*\x12z\n\x04stat\x12..spaceone.api.secret.v1.TrustedSecretStatQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"\x1e/secret/v1/trusted-secret/stat:\x01*B=Z;github.com/cloudforet-io/api/dist/go/spaceone/api/secret/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.secret.v1.trusted_secret_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z;github.com/cloudforet-io/api/dist/go/spaceone/api/secret/v1'
  _TRUSTEDSECRET.methods_by_name['create']._options = None
  _TRUSTEDSECRET.methods_by_name['create']._serialized_options = b'\202\323\344\223\002%\" /secret/v1/trusted-secret/create:\001*'
  _TRUSTEDSECRET.methods_by_name['update']._options = None
  _TRUSTEDSECRET.methods_by_name['update']._serialized_options = b'\202\323\344\223\002%\" /secret/v1/trusted-secret/update:\001*'
  _TRUSTEDSECRET.methods_by_name['delete']._options = None
  _TRUSTEDSECRET.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002%\" /secret/v1/trusted-secret/delete:\001*'
  _TRUSTEDSECRET.methods_by_name['update_data']._options = None
  _TRUSTEDSECRET.methods_by_name['update_data']._serialized_options = b'\202\323\344\223\002*\"%/secret/v1/trusted-secret/update-data:\001*'
  _TRUSTEDSECRET.methods_by_name['get']._options = None
  _TRUSTEDSECRET.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\"\"\035/secret/v1/trusted-secret/get:\001*'
  _TRUSTEDSECRET.methods_by_name['list']._options = None
  _TRUSTEDSECRET.methods_by_name['list']._serialized_options = b'\202\323\344\223\002#\"\036/secret/v1/trusted-secret/list:\001*'
  _TRUSTEDSECRET.methods_by_name['stat']._options = None
  _TRUSTEDSECRET.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002#\"\036/secret/v1/trusted-secret/stat:\001*'
  _globals['_CREATETRUSTEDSECRETREQUEST']._serialized_start=195
  _globals['_CREATETRUSTEDSECRETREQUEST']._serialized_end=378
  _globals['_UPDATETRUSTEDSECRETREQUEST']._serialized_start=380
  _globals['_UPDATETRUSTEDSECRETREQUEST']._serialized_end=507
  _globals['_TRUSTEDSECRETREQUEST']._serialized_start=509
  _globals['_TRUSTEDSECRETREQUEST']._serialized_end=577
  _globals['_UPDATETRUSTEDSECRETDATAREQUEST']._serialized_start=580
  _globals['_UPDATETRUSTEDSECRETDATAREQUEST']._serialized_end=713
  _globals['_GETTRUSTEDSECRETREQUEST']._serialized_start=715
  _globals['_GETTRUSTEDSECRETREQUEST']._serialized_end=800
  _globals['_TRUSTEDSECRETQUERY']._serialized_start=803
  _globals['_TRUSTEDSECRETQUERY']._serialized_end=989
  _globals['_TRUSTEDSECRETINFO']._serialized_start=992
  _globals['_TRUSTEDSECRETINFO']._serialized_end=1212
  _globals['_TRUSTEDSECRETSINFO']._serialized_start=1214
  _globals['_TRUSTEDSECRETSINFO']._serialized_end=1315
  _globals['_TRUSTEDSECRETSTATQUERY']._serialized_start=1317
  _globals['_TRUSTEDSECRETSTATQUERY']._serialized_end=1414
  _globals['_TRUSTEDSECRET']._serialized_start=1417
  _globals['_TRUSTEDSECRET']._serialized_end=2411
# @@protoc_insertion_point(module_scope)
