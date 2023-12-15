# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v2/token.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$spaceone/api/identity/v2/token.proto\x12\x18spaceone.api.identity.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf2\x01\n\x11IssueTokenRequest\x12,\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12G\n\tauth_type\x18\x02 \x01(\x0e\x32\x34.spaceone.api.identity.v2.IssueTokenRequest.AuthType\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x12\x13\n\x0bverify_code\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"-\n\x08\x41uthType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02\"8\n\tTokenInfo\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\"\xde\x02\n\x11GrantTokenRequest\x12I\n\ngrant_type\x18\x01 \x01(\x0e\x32\x35.spaceone.api.identity.v2.GrantTokenRequest.GrantType\x12\r\n\x05token\x18\x02 \x01(\t\x12@\n\x05scope\x18\x03 \x01(\x0e\x32\x31.spaceone.api.identity.v2.GrantTokenRequest.Scope\x12\x14\n\x0cworkspace_id\x18\x04 \x01(\t\"@\n\tGrantType\x12\x13\n\x0fGRANT_TYPE_NONE\x10\x00\x12\x0b\n\x07\x41PI_KEY\x10\x01\x12\x11\n\rREFRESH_TOKEN\x10\x02\"U\n\x05Scope\x12\x0e\n\nSCOPE_NONE\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\n\n\x06\x44OMAIN\x10\x02\x12\r\n\tWORKSPACE\x10\x03\x12\x0b\n\x07PROJECT\x10\x04\x12\x08\n\x04USER\x10\x05\"\x9f\x02\n\x0eGrantTokenInfo\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\t\x12\x44\n\trole_type\x18\x03 \x01(\x0e\x32\x31.spaceone.api.identity.v2.GrantTokenInfo.RoleType\x12\x14\n\x0cworkspace_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"w\n\x08RoleType\x12\x12\n\x0eROLE_TYPE_NONE\x10\x00\x12\x10\n\x0cSYSTEM_ADMIN\x10\x01\x12\x10\n\x0c\x44OMAIN_ADMIN\x10\x02\x12\x13\n\x0fWORKSPACE_OWNER\x10\x03\x12\x14\n\x10WORKSPACE_MEMBER\x10\x04\x12\x08\n\x04USER\x10\x05\x32\x8d\x02\n\x05Token\x12~\n\x05issue\x12+.spaceone.api.identity.v2.IssueTokenRequest\x1a#.spaceone.api.identity.v2.TokenInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v2/token/issue:\x01*\x12\x83\x01\n\x05grant\x12+.spaceone.api.identity.v2.GrantTokenRequest\x1a(.spaceone.api.identity.v2.GrantTokenInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v2/token/grant:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v2.token_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v2'
  _globals['_TOKEN'].methods_by_name['issue']._options = None
  _globals['_TOKEN'].methods_by_name['issue']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v2/token/issue:\001*'
  _globals['_TOKEN'].methods_by_name['grant']._options = None
  _globals['_TOKEN'].methods_by_name['grant']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v2/token/grant:\001*'
  _globals['_ISSUETOKENREQUEST']._serialized_start=156
  _globals['_ISSUETOKENREQUEST']._serialized_end=398
  _globals['_ISSUETOKENREQUEST_AUTHTYPE']._serialized_start=353
  _globals['_ISSUETOKENREQUEST_AUTHTYPE']._serialized_end=398
  _globals['_TOKENINFO']._serialized_start=400
  _globals['_TOKENINFO']._serialized_end=456
  _globals['_GRANTTOKENREQUEST']._serialized_start=459
  _globals['_GRANTTOKENREQUEST']._serialized_end=809
  _globals['_GRANTTOKENREQUEST_GRANTTYPE']._serialized_start=658
  _globals['_GRANTTOKENREQUEST_GRANTTYPE']._serialized_end=722
  _globals['_GRANTTOKENREQUEST_SCOPE']._serialized_start=724
  _globals['_GRANTTOKENREQUEST_SCOPE']._serialized_end=809
  _globals['_GRANTTOKENINFO']._serialized_start=812
  _globals['_GRANTTOKENINFO']._serialized_end=1099
  _globals['_GRANTTOKENINFO_ROLETYPE']._serialized_start=980
  _globals['_GRANTTOKENINFO_ROLETYPE']._serialized_end=1099
  _globals['_TOKEN']._serialized_start=1102
  _globals['_TOKEN']._serialized_end=1371
# @@protoc_insertion_point(module_scope)
