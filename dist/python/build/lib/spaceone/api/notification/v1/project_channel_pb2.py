# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/notification/v1/project_channel.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2spaceone/api/notification/v1/project_channel.proto\x12\x1cspaceone.api.notification.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xe9\x01\n\x16ProjectChannelSchedule\x12S\n\x0b\x64\x61y_of_week\x18\x01 \x03(\x0e\x32>.spaceone.api.notification.v1.ProjectChannelSchedule.DayOfWeek\x12\x12\n\nstart_hour\x18\x02 \x01(\x05\x12\x10\n\x08\x65nd_hour\x18\x03 \x01(\x05\"T\n\tDayOfWeek\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03MON\x10\x01\x12\x07\n\x03TUE\x10\x02\x12\x07\n\x03WED\x10\x03\x12\x07\n\x03THU\x10\x04\x12\x07\n\x03\x46RI\x10\x05\x12\x07\n\x03SAT\x10\x06\x12\x07\n\x03SUN\x10\x07\"\xfa\x02\n\x1b\x43reateProjectChannelRequest\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0cis_subscribe\x18\x04 \x01(\x08\x12\x15\n\rsubscriptions\x18\x05 \x03(\t\x12K\n\x12notification_level\x18\x06 \x01(\x0e\x32/.spaceone.api.notification.v1.NotificationLevel\x12\x14\n\x0cis_scheduled\x18\x07 \x01(\x08\x12\x46\n\x08schedule\x18\x08 \x01(\x0b\x32\x34.spaceone.api.notification.v1.ProjectChannelSchedule\x12%\n\x04tags\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x15 \x01(\t\"\xf5\x01\n\x1bUpdateProjectChannelRequest\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12K\n\x12notification_level\x18\x05 \x01(\x0e\x32/.spaceone.api.notification.v1.NotificationLevel\x12%\n\x04tags\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\x9f\x01\n#UpdateProjectChannelScheduleRequest\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\x12\x14\n\x0cis_scheduled\x18\x02 \x01(\x08\x12\x46\n\x08schedule\x18\x03 \x01(\x0b\x32\x34.spaceone.api.notification.v1.ProjectChannelSchedule\"r\n\'UpdateProjectChannelSubscriptionRequest\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\x12\x14\n\x0cis_subscribe\x18\x02 \x01(\x08\x12\x15\n\rsubscriptions\x18\x03 \x03(\t\"3\n\x15ProjectChannelRequest\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\"6\n\x18GetProjectChannelRequest\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\"\x9c\x03\n\x13ProjectChannelQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x1a\n\x12project_channel_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12T\n\x05state\x18\x04 \x01(\x0e\x32\x45.spaceone.api.notification.v1.ProjectChannelQuery.ProjectChannelState\x12\x11\n\tsecret_id\x18\x05 \x01(\t\x12\x14\n\x0cis_scheduled\x18\x06 \x01(\x08\x12K\n\x12notification_level\x18\x07 \x01(\x0e\x32/.spaceone.api.notification.v1.NotificationLevel\x12\x13\n\x0bprotocol_id\x18\x0b \x01(\t\x12\x12\n\nproject_id\x18\x0c \x01(\t\":\n\x13ProjectChannelState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xee\x04\n\x12ProjectChannelInfo\x12\x1a\n\x12project_channel_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12S\n\x05state\x18\x03 \x01(\x0e\x32\x44.spaceone.api.notification.v1.ProjectChannelInfo.ProjectChannelState\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tsecret_id\x18\x05 \x01(\t\x12\x14\n\x0cis_subscribe\x18\x06 \x01(\x08\x12\x15\n\rsubscriptions\x18\x07 \x03(\t\x12K\n\x12notification_level\x18\x08 \x01(\x0e\x32/.spaceone.api.notification.v1.NotificationLevel\x12\x14\n\x0cis_scheduled\x18\t \x01(\x08\x12\x46\n\x08schedule\x18\n \x01(\x0b\x32\x34.spaceone.api.notification.v1.ProjectChannelSchedule\x12%\n\x04tags\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0bprotocol_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x16 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x17 \x01(\t\x12\x11\n\tdomain_id\x18\x18 \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\":\n\x13ProjectChannelState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"m\n\x13ProjectChannelsInfo\x12\x41\n\x07results\x18\x01 \x03(\x0b\x32\x30.spaceone.api.notification.v1.ProjectChannelInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"b\n\x17ProjectChannelStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t*J\n\x11NotificationLevel\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03LV1\x10\x01\x12\x07\n\x03LV2\x10\x02\x12\x07\n\x03LV3\x10\x03\x12\x07\n\x03LV4\x10\x04\x12\x07\n\x03LV5\x10\x05\x32\x9d\r\n\x0eProjectChannel\x12\xa9\x01\n\x06\x63reate\x12\x39.spaceone.api.notification.v1.CreateProjectChannelRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"2\x82\xd3\xe4\x93\x02,\"\'/notification/v1/project-channel/create:\x01*\x12\xa9\x01\n\x06update\x12\x39.spaceone.api.notification.v1.UpdateProjectChannelRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"2\x82\xd3\xe4\x93\x02,\"\'/notification/v1/project-channel/update:\x01*\x12\xbd\x01\n\x0cset_schedule\x12\x41.spaceone.api.notification.v1.UpdateProjectChannelScheduleRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"8\x82\xd3\xe4\x93\x02\x32\"-/notification/v1/project-channel/set-schedule:\x01*\x12\xc9\x01\n\x10set_subscription\x12\x45.spaceone.api.notification.v1.UpdateProjectChannelSubscriptionRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"<\x82\xd3\xe4\x93\x02\x36\"1/notification/v1/project-channel/set-subscription:\x01*\x12\xa3\x01\n\x06\x65nable\x12\x33.spaceone.api.notification.v1.ProjectChannelRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"2\x82\xd3\xe4\x93\x02,\"\'/notification/v1/project-channel/enable:\x01*\x12\xa5\x01\n\x07\x64isable\x12\x33.spaceone.api.notification.v1.ProjectChannelRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"3\x82\xd3\xe4\x93\x02-\"(/notification/v1/project-channel/disable:\x01*\x12\x89\x01\n\x06\x64\x65lete\x12\x33.spaceone.api.notification.v1.ProjectChannelRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/notification/v1/project-channel/delete:\x01*\x12\xa0\x01\n\x03get\x12\x36.spaceone.api.notification.v1.GetProjectChannelRequest\x1a\x30.spaceone.api.notification.v1.ProjectChannelInfo\"/\x82\xd3\xe4\x93\x02)\"$/notification/v1/project-channel/get:\x01*\x12\x9e\x01\n\x04list\x12\x31.spaceone.api.notification.v1.ProjectChannelQuery\x1a\x31.spaceone.api.notification.v1.ProjectChannelsInfo\"0\x82\xd3\xe4\x93\x02*\"%/notification/v1/project-channel/list:\x01*\x12\x88\x01\n\x04stat\x12\x35.spaceone.api.notification.v1.ProjectChannelStatQuery\x1a\x17.google.protobuf.Struct\"0\x82\xd3\xe4\x93\x02*\"%/notification/v1/project-channel/stat:\x01*BCZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/notification/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.notification.v1.project_channel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/cloudforet-io/api/dist/go/spaceone/api/notification/v1'
  _globals['_PROJECTCHANNEL'].methods_by_name['create']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['create']._serialized_options = b'\202\323\344\223\002,\"\'/notification/v1/project-channel/create:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['update']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['update']._serialized_options = b'\202\323\344\223\002,\"\'/notification/v1/project-channel/update:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['set_schedule']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['set_schedule']._serialized_options = b'\202\323\344\223\0022\"-/notification/v1/project-channel/set-schedule:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['set_subscription']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['set_subscription']._serialized_options = b'\202\323\344\223\0026\"1/notification/v1/project-channel/set-subscription:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['enable']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['enable']._serialized_options = b'\202\323\344\223\002,\"\'/notification/v1/project-channel/enable:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['disable']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['disable']._serialized_options = b'\202\323\344\223\002-\"(/notification/v1/project-channel/disable:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['delete']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['delete']._serialized_options = b'\202\323\344\223\002,\"\'/notification/v1/project-channel/delete:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['get']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['get']._serialized_options = b'\202\323\344\223\002)\"$/notification/v1/project-channel/get:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['list']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002*\"%/notification/v1/project-channel/list:\001*'
  _globals['_PROJECTCHANNEL'].methods_by_name['stat']._options = None
  _globals['_PROJECTCHANNEL'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002*\"%/notification/v1/project-channel/stat:\001*'
  _globals['_NOTIFICATIONLEVEL']._serialized_start=2710
  _globals['_NOTIFICATIONLEVEL']._serialized_end=2784
  _globals['_PROJECTCHANNELSCHEDULE']._serialized_start=208
  _globals['_PROJECTCHANNELSCHEDULE']._serialized_end=441
  _globals['_PROJECTCHANNELSCHEDULE_DAYOFWEEK']._serialized_start=357
  _globals['_PROJECTCHANNELSCHEDULE_DAYOFWEEK']._serialized_end=441
  _globals['_CREATEPROJECTCHANNELREQUEST']._serialized_start=444
  _globals['_CREATEPROJECTCHANNELREQUEST']._serialized_end=822
  _globals['_UPDATEPROJECTCHANNELREQUEST']._serialized_start=825
  _globals['_UPDATEPROJECTCHANNELREQUEST']._serialized_end=1070
  _globals['_UPDATEPROJECTCHANNELSCHEDULEREQUEST']._serialized_start=1073
  _globals['_UPDATEPROJECTCHANNELSCHEDULEREQUEST']._serialized_end=1232
  _globals['_UPDATEPROJECTCHANNELSUBSCRIPTIONREQUEST']._serialized_start=1234
  _globals['_UPDATEPROJECTCHANNELSUBSCRIPTIONREQUEST']._serialized_end=1348
  _globals['_PROJECTCHANNELREQUEST']._serialized_start=1350
  _globals['_PROJECTCHANNELREQUEST']._serialized_end=1401
  _globals['_GETPROJECTCHANNELREQUEST']._serialized_start=1403
  _globals['_GETPROJECTCHANNELREQUEST']._serialized_end=1457
  _globals['_PROJECTCHANNELQUERY']._serialized_start=1460
  _globals['_PROJECTCHANNELQUERY']._serialized_end=1872
  _globals['_PROJECTCHANNELQUERY_PROJECTCHANNELSTATE']._serialized_start=1814
  _globals['_PROJECTCHANNELQUERY_PROJECTCHANNELSTATE']._serialized_end=1872
  _globals['_PROJECTCHANNELINFO']._serialized_start=1875
  _globals['_PROJECTCHANNELINFO']._serialized_end=2497
  _globals['_PROJECTCHANNELINFO_PROJECTCHANNELSTATE']._serialized_start=1814
  _globals['_PROJECTCHANNELINFO_PROJECTCHANNELSTATE']._serialized_end=1872
  _globals['_PROJECTCHANNELSINFO']._serialized_start=2499
  _globals['_PROJECTCHANNELSINFO']._serialized_end=2608
  _globals['_PROJECTCHANNELSTATQUERY']._serialized_start=2610
  _globals['_PROJECTCHANNELSTATQUERY']._serialized_end=2708
  _globals['_PROJECTCHANNEL']._serialized_start=2787
  _globals['_PROJECTCHANNEL']._serialized_end=4480
# @@protoc_insertion_point(module_scope)
