# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_analysis/v1/cost_report_data.proto
# Protobuf Python Version: 4.25.1
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
from spaceone.api.core.v2 import query_pb2 as spaceone_dot_api_dot_core_dot_v2_dot_query__pb2
from spaceone.api.cost_analysis.v1 import job_pb2 as spaceone_dot_api_dot_cost__analysis_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4spaceone/api/cost_analysis/v1/cost_report_data.proto\x12\x1dspaceone.api.cost_analysis.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a spaceone/api/core/v2/query.proto\x1a\'spaceone/api/cost_analysis/v1/job.proto\"\xfc\x01\n\x13\x43ostReportDataQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v2.Query\x12\x1b\n\x13\x63ost_report_data_id\x18\x02 \x01(\t\x12\x0f\n\x07product\x18\x03 \x01(\t\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x14\n\x0cis_confirmed\x18\x05 \x01(\x08\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x1d\n\x15\x63ost_report_config_id\x18\x16 \x01(\t\x12\x16\n\x0e\x63ost_report_id\x18\x17 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x18 \x01(\t\"\xdf\x01\n\x1a\x43ostReportDataAnalyzeQuery\x12;\n\x05query\x18\x01 \x01(\x0b\x32,.spaceone.api.core.v2.TimeSeriesAnalyzeQuery\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x14\n\x0cis_confirmed\x18\x04 \x01(\x08\x12\x14\n\x0cworkspace_id\x18\x15 \x01(\t\x12\x1d\n\x15\x63ost_report_config_id\x18\x16 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x17 \x01(\t\"\x8c\x04\n\x12\x43ostReportDataInfo\x12\x1b\n\x13\x63ost_report_data_id\x18\x01 \x01(\t\x12%\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x10\x63ost_report_name\x18\x03 \x01(\t\x12\x12\n\nissue_date\x18\x04 \x01(\t\x12\x13\n\x0breport_year\x18\x05 \x01(\t\x12\x14\n\x0creport_month\x18\x06 \x01(\t\x12\x14\n\x0cis_confirmed\x18\x07 \x01(\x08\x12\x10\n\x08provider\x18\x08 \x01(\t\x12\x0f\n\x07product\x18\t \x01(\t\x12\x1c\n\x14service_account_name\x18\n \x01(\t\x12\x18\n\x10\x64\x61ta_source_name\x18\x0b \x01(\t\x12\x14\n\x0cproject_name\x18\x0c \x01(\t\x12\x16\n\x0eworkspace_name\x18\r \x01(\t\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x16 \x01(\t\x12\x12\n\nproject_id\x18\x17 \x01(\t\x12\x1d\n\x15\x63ost_report_config_id\x18\x18 \x01(\t\x12\x16\n\x0e\x63ost_report_id\x18\x19 \x01(\t\x12\x16\n\x0e\x64\x61ta_source_id\x18\x1a \x01(\t\x12\x1a\n\x12service_account_id\x18\x1b \x01(\t\x12\x12\n\ncreated_at\x18\x1f \x01(\t\"n\n\x13\x43ostReportsDataInfo\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.spaceone.api.cost_analysis.v1.CostReportDataInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"\x86\x01\n\x17\x43ostReportDataStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v2.StatisticsQuery\x12\x16\n\x0e\x63ost_report_id\x18\x15 \x01(\t\x12\x1d\n\x15\x63ost_report_config_id\x18\x16 \x01(\t2\xda\x03\n\x0e\x43ostReportData\x12\xa2\x01\n\x04list\x12\x32.spaceone.api.cost_analysis.v1.CostReportDataQuery\x1a\x32.spaceone.api.cost_analysis.v1.CostReportsDataInfo\"2\x82\xd3\xe4\x93\x02,\"\'/cost-analysis/v1/cost-report-data/list:\x01*\x12\x94\x01\n\x07\x61nalyze\x12\x39.spaceone.api.cost_analysis.v1.CostReportDataAnalyzeQuery\x1a\x17.google.protobuf.Struct\"5\x82\xd3\xe4\x93\x02/\"*/cost-analysis/v1/cost-report-data/analyze:\x01*\x12\x8b\x01\n\x04stat\x12\x36.spaceone.api.cost_analysis.v1.CostReportDataStatQuery\x1a\x17.google.protobuf.Struct\"2\x82\xd3\xe4\x93\x02,\"\'/cost-analysis/v1/cost-report-data/stat:\x01*BDZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spaceone.api.cost_analysis.v1.cost_report_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/cloudforet-io/api/dist/go/spaceone/api/cost_analysis/v1'
  _globals['_COSTREPORTDATA'].methods_by_name['list']._options = None
  _globals['_COSTREPORTDATA'].methods_by_name['list']._serialized_options = b'\202\323\344\223\002,\"\'/cost-analysis/v1/cost-report-data/list:\001*'
  _globals['_COSTREPORTDATA'].methods_by_name['analyze']._options = None
  _globals['_COSTREPORTDATA'].methods_by_name['analyze']._serialized_options = b'\202\323\344\223\002/\"*/cost-analysis/v1/cost-report-data/analyze:\001*'
  _globals['_COSTREPORTDATA'].methods_by_name['stat']._options = None
  _globals['_COSTREPORTDATA'].methods_by_name['stat']._serialized_options = b'\202\323\344\223\002,\"\'/cost-analysis/v1/cost-report-data/stat:\001*'
  _globals['_COSTREPORTDATAQUERY']._serialized_start=252
  _globals['_COSTREPORTDATAQUERY']._serialized_end=504
  _globals['_COSTREPORTDATAANALYZEQUERY']._serialized_start=507
  _globals['_COSTREPORTDATAANALYZEQUERY']._serialized_end=730
  _globals['_COSTREPORTDATAINFO']._serialized_start=733
  _globals['_COSTREPORTDATAINFO']._serialized_end=1257
  _globals['_COSTREPORTSDATAINFO']._serialized_start=1259
  _globals['_COSTREPORTSDATAINFO']._serialized_end=1369
  _globals['_COSTREPORTDATASTATQUERY']._serialized_start=1372
  _globals['_COSTREPORTDATASTATQUERY']._serialized_end=1506
  _globals['_COSTREPORTDATA']._serialized_start=1509
  _globals['_COSTREPORTDATA']._serialized_end=1983
# @@protoc_insertion_point(module_scope)