# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/domain.proto
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
from spaceone.api.core.v1 import handler_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%spaceone/api/identity/v1/domain.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a\"spaceone/api/core/v1/handler.proto\"\xae\x01\n\x13\x43reateDomainRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x0bplugin_info\x18\x02 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xb3\x01\n\x13UpdateDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x39\n\x0bplugin_info\x18\x02 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"~\n\x11\x43hangeAuthRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x39\n\x0bplugin_info\x18\x02 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\x1b\n\x13release_auth_plugin\x18\x03 \x01(\x08\"\xe3\x01\n\x13UpdatePluginRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12O\n\x0cupgrade_mode\x18\x04 \x01(\x0e\x32\x39.spaceone.api.identity.v1.UpdatePluginRequest.UpgradeMode\"-\n\x0bUpgradeMode\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"\"\n\rDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\"3\n\x10GetDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x0c\n\x04only\x18\x02 \x03(\t\"\xc4\x01\n\x0b\x44omainQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12:\n\x05state\x18\x04 \x01(\x0e\x32+.spaceone.api.identity.v1.DomainQuery.State\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xc9\x02\n\nDomainInfo\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\x05state\x18\x03 \x01(\x0e\x32*.spaceone.api.identity.v1.DomainInfo.State\x12\x39\n\x0bplugin_info\x18\x04 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\ncreated_at\x18\x07 \x01(\t\x12\x12\n\ndeleted_at\x18\x08 \x01(\t\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"Y\n\x0b\x44omainsInfo\x12\x35\n\x07results\x18\x01 \x03(\x0b\x32$.spaceone.api.identity.v1.DomainInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"G\n\x0f\x44omainStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\"\xcd\x02\n\nPluginInfo\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x11\n\tsecret_id\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bsecret_data\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x06 \x01(\t\x12)\n\x08metadata\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x46\n\x0cupgrade_mode\x18\x08 \x01(\x0e\x32\x30.spaceone.api.identity.v1.PluginInfo.UpgradeMode\"-\n\x0bUpgradeMode\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x32\xc3\x0c\n\x06\x44omain\x12\x84\x01\n\x06\x63reate\x12-.spaceone.api.identity.v1.CreateDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/identity/v1/domain/create:\x01*\x12\x84\x01\n\x06update\x12-.spaceone.api.identity.v1.UpdateDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/identity/v1/domain/update:\x01*\x12\x9a\x01\n\x12\x63hange_auth_plugin\x12+.spaceone.api.identity.v1.ChangeAuthRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"1\x82\xd3\xe4\x93\x02+\"&/identity/v1/domain/change-auth-plugin:\x01*\x12\x92\x01\n\rupdate_plugin\x12-.spaceone.api.identity.v1.UpdatePluginRequest\x1a$.spaceone.api.identity.v1.DomainInfo\",\x82\xd3\xe4\x93\x02&\"!/identity/v1/domain/update-plugin:\x01*\x12~\n\rverify_plugin\x12\'.spaceone.api.identity.v1.DomainRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&\"!/identity/v1/domain/verify-plugin:\x01*\x12p\n\x06\x64\x65lete\x12\'.spaceone.api.identity.v1.DomainRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/identity/v1/domain/delete:\x01*\x12~\n\x06\x65nable\x12\'.spaceone.api.identity.v1.DomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/identity/v1/domain/enable:\x01*\x12\x80\x01\n\x07\x64isable\x12\'.spaceone.api.identity.v1.DomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"&\x82\xd3\xe4\x93\x02 \"\x1b/identity/v1/domain/disable:\x01*\x12{\n\x03get\x12*.spaceone.api.identity.v1.GetDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/identity/v1/domain/get:\x01*\x12y\n\x04list\x12%.spaceone.api.identity.v1.DomainQuery\x1a%.spaceone.api.identity.v1.DomainsInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v1/domain/list:\x01*\x12o\n\x04stat\x12).spaceone.api.identity.v1.DomainStatQuery\x1a\x17.google.protobuf.Struct\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/identity/v1/domain/stat:\x01*\x12\x9a\x01\n\x0eget_public_key\x12+.spaceone.api.core.v1.AuthenticationRequest\x1a,.spaceone.api.core.v1.AuthenticationResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/identity/v1/domain/get-public-key:\x01*B?Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.identity.v1.domain_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z=github.com/cloudforet-io/api/dist/go/spaceone/api/identity/v1'
  _DOMAIN.methods_by_name['create']._options = None
  _DOMAIN.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\037\"\032/identity/v1/domain/create:\001*'
  _DOMAIN.methods_by_name['update']._options = None
  _DOMAIN.methods_by_name['update']._serialized_options = b'\202\323\344\223\002\037\"\032/identity/v1/domain/update:\001*'
  _DOMAIN.methods_by_name['change_auth_plugin']._options = None
  _DOMAIN.methods_by_name['change_auth_plugin']._serialized_options = b'\202\323\344\223\002+\"&/identity/v1/domain/change-auth-plugin:\001*'
  _DOMAIN.methods_by_name['update_plugin']._options = None
  _DOMAIN.methods_by_name['update_plugin']._serialized_options = b'\202\323\344\223\002&\"!/identity/v1/domain/update-plugin:\001*'
  _DOMAIN.methods_by_name['verify_plugin']._options = None
  _DOMAIN.methods_by_name['verify_plugin']._serialized_options = b'\202\323\344\223\002&\"!/identity/v1/domain/verify-plugin:\001*'
  _DOMAIN.methods_by_name['delete']._options = None
  _DOMAIN.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\037\"\032/identity/v1/domain/delete:\001*'
  _DOMAIN.methods_by_name['enable']._options = None
  _DOMAIN.methods_by_name['enable']._serialized_options = b'\202\323\344\223\002\037\"\032/identity/v1/domain/enable:\001*'
  _DOMAIN.methods_by_name['disable']._options = None
  _DOMAIN.methods_by_name['disable']._serialized_options = b'\202\323\344\223\002 \"\033/identity/v1/domain/disable:\001*'
  _DOMAIN.methods_by_name['get']._options = None
  _DOMAIN.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\034\"\027/identity/v1/domain/get:\001*'
  _DOMAIN.methods_by_name['list']._options = None
  _DOMAIN.methods_by_name['list']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v1/domain/list:\001*'
  _DOMAIN.methods_by_name['stat']._options = None
  _DOMAIN.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\035\"\030/identity/v1/domain/stat:\001*'
  _DOMAIN.methods_by_name['get_public_key']._options = None
  _DOMAIN.methods_by_name['get_public_key']._serialized_options = b'\202\323\344\223\002\'\"\"/identity/v1/domain/get-public-key:\001*'
  _globals['_CREATEDOMAINREQUEST']._serialized_start=227
  _globals['_CREATEDOMAINREQUEST']._serialized_end=401
  _globals['_UPDATEDOMAINREQUEST']._serialized_start=404
  _globals['_UPDATEDOMAINREQUEST']._serialized_end=583
  _globals['_CHANGEAUTHREQUEST']._serialized_start=585
  _globals['_CHANGEAUTHREQUEST']._serialized_end=711
  _globals['_UPDATEPLUGINREQUEST']._serialized_start=714
  _globals['_UPDATEPLUGINREQUEST']._serialized_end=941
  _globals['_UPDATEPLUGINREQUEST_UPGRADEMODE']._serialized_start=896
  _globals['_UPDATEPLUGINREQUEST_UPGRADEMODE']._serialized_end=941
  _globals['_DOMAINREQUEST']._serialized_start=943
  _globals['_DOMAINREQUEST']._serialized_end=977
  _globals['_GETDOMAINREQUEST']._serialized_start=979
  _globals['_GETDOMAINREQUEST']._serialized_end=1030
  _globals['_DOMAINQUERY']._serialized_start=1033
  _globals['_DOMAINQUERY']._serialized_end=1229
  _globals['_DOMAINQUERY_STATE']._serialized_start=1185
  _globals['_DOMAINQUERY_STATE']._serialized_end=1229
  _globals['_DOMAININFO']._serialized_start=1232
  _globals['_DOMAININFO']._serialized_end=1561
  _globals['_DOMAININFO_STATE']._serialized_start=1185
  _globals['_DOMAININFO_STATE']._serialized_end=1229
  _globals['_DOMAINSINFO']._serialized_start=1563
  _globals['_DOMAINSINFO']._serialized_end=1652
  _globals['_DOMAINSTATQUERY']._serialized_start=1654
  _globals['_DOMAINSTATQUERY']._serialized_end=1725
  _globals['_PLUGININFO']._serialized_start=1728
  _globals['_PLUGININFO']._serialized_end=2061
  _globals['_PLUGININFO_UPGRADEMODE']._serialized_start=896
  _globals['_PLUGININFO_UPGRADEMODE']._serialized_end=941
  _globals['_DOMAIN']._serialized_start=2064
  _globals['_DOMAIN']._serialized_end=3667
# @@protoc_insertion_point(module_scope)
