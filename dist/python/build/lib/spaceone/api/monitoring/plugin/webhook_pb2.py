# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/plugin/webhook.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,spaceone/api/monitoring/plugin/webhook.proto\x12\x1espaceone.api.monitoring.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\">\n\x12WebhookInitRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"F\n\x1aWebhookPluginVerifyRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\">\n\x11WebhookPluginInfo\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\xda\x01\n\x07Webhook\x12o\n\x04init\x12\x32.spaceone.api.monitoring.plugin.WebhookInitRequest\x1a\x31.spaceone.api.monitoring.plugin.WebhookPluginInfo\"\x00\x12^\n\x06verify\x12:.spaceone.api.monitoring.plugin.WebhookPluginVerifyRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\x45ZCgithub.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/pluginb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.monitoring.plugin.webhook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZCgithub.com/cloudforet-io/api/dist/go/spaceone/api/monitoring/plugin'
  _globals['_WEBHOOKINITREQUEST']._serialized_start=139
  _globals['_WEBHOOKINITREQUEST']._serialized_end=201
  _globals['_WEBHOOKPLUGINVERIFYREQUEST']._serialized_start=203
  _globals['_WEBHOOKPLUGINVERIFYREQUEST']._serialized_end=273
  _globals['_WEBHOOKPLUGININFO']._serialized_start=275
  _globals['_WEBHOOKPLUGININFO']._serialized_end=337
  _globals['_WEBHOOK']._serialized_start=340
  _globals['_WEBHOOK']._serialized_end=558
# @@protoc_insertion_point(module_scope)
