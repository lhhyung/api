// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/inventory/v1/metric_data.proto

package v1

import (
	context "context"
	_struct "github.com/golang/protobuf/ptypes/struct"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.62.0 or later.
const _ = grpc.SupportPackageIsVersion8

const (
	MetricData_List_FullMethodName    = "/spaceone.api.inventory.v1.MetricData/list"
	MetricData_Stat_FullMethodName    = "/spaceone.api.inventory.v1.MetricData/stat"
	MetricData_Analyze_FullMethodName = "/spaceone.api.inventory.v1.MetricData/analyze"
)

// MetricDataClient is the client API for MetricData service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MetricDataClient interface {
	List(ctx context.Context, in *MetricDataQuery, opts ...grpc.CallOption) (*MetricDatasInfo, error)
	Stat(ctx context.Context, in *MetricDataStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
	Analyze(ctx context.Context, in *MetricDataAnalyzeQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type metricDataClient struct {
	cc grpc.ClientConnInterface
}

func NewMetricDataClient(cc grpc.ClientConnInterface) MetricDataClient {
	return &metricDataClient{cc}
}

func (c *metricDataClient) List(ctx context.Context, in *MetricDataQuery, opts ...grpc.CallOption) (*MetricDatasInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(MetricDatasInfo)
	err := c.cc.Invoke(ctx, MetricData_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *metricDataClient) Stat(ctx context.Context, in *MetricDataStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, MetricData_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *metricDataClient) Analyze(ctx context.Context, in *MetricDataAnalyzeQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, MetricData_Analyze_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MetricDataServer is the server API for MetricData service.
// All implementations must embed UnimplementedMetricDataServer
// for forward compatibility
type MetricDataServer interface {
	List(context.Context, *MetricDataQuery) (*MetricDatasInfo, error)
	Stat(context.Context, *MetricDataStatQuery) (*_struct.Struct, error)
	Analyze(context.Context, *MetricDataAnalyzeQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedMetricDataServer()
}

// UnimplementedMetricDataServer must be embedded to have forward compatible implementations.
type UnimplementedMetricDataServer struct {
}

func (UnimplementedMetricDataServer) List(context.Context, *MetricDataQuery) (*MetricDatasInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedMetricDataServer) Stat(context.Context, *MetricDataStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedMetricDataServer) Analyze(context.Context, *MetricDataAnalyzeQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Analyze not implemented")
}
func (UnimplementedMetricDataServer) mustEmbedUnimplementedMetricDataServer() {}

// UnsafeMetricDataServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to MetricDataServer will
// result in compilation errors.
type UnsafeMetricDataServer interface {
	mustEmbedUnimplementedMetricDataServer()
}

func RegisterMetricDataServer(s grpc.ServiceRegistrar, srv MetricDataServer) {
	s.RegisterService(&MetricData_ServiceDesc, srv)
}

func _MetricData_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricDataQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MetricDataServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: MetricData_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MetricDataServer).List(ctx, req.(*MetricDataQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _MetricData_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricDataStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MetricDataServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: MetricData_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MetricDataServer).Stat(ctx, req.(*MetricDataStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _MetricData_Analyze_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricDataAnalyzeQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MetricDataServer).Analyze(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: MetricData_Analyze_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MetricDataServer).Analyze(ctx, req.(*MetricDataAnalyzeQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// MetricData_ServiceDesc is the grpc.ServiceDesc for MetricData service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var MetricData_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.inventory.v1.MetricData",
	HandlerType: (*MetricDataServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "list",
			Handler:    _MetricData_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _MetricData_Stat_Handler,
		},
		{
			MethodName: "analyze",
			Handler:    _MetricData_Analyze_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/inventory/v1/metric_data.proto",
}
