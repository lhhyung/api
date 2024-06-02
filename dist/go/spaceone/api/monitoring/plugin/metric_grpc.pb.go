// A Metric is a monitoring metric data delivered from an external cloud service via a DataSource.

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/monitoring/plugin/metric.proto

package plugin

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.62.0 or later.
const _ = grpc.SupportPackageIsVersion8

const (
	Metric_List_FullMethodName    = "/spaceone.api.monitoring.plugin.Metric/list"
	Metric_GetData_FullMethodName = "/spaceone.api.monitoring.plugin.Metric/get_data"
)

// MetricClient is the client API for Metric service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MetricClient interface {
	// Gets a list of all Metrics from a specific cloud service. You can use the method to list up the Metrics to collect before using the `get_data` method to collect the Metrics.
	List(ctx context.Context, in *MetricRequest, opts ...grpc.CallOption) (*MetricsInfo, error)
	// Gets a Metric from a specific cloud service resource `instance`. By specifying the time period to collect the Metric, the Metric data value of the `instance` during the period is returned.
	GetData(ctx context.Context, in *MetricDataRequest, opts ...grpc.CallOption) (*MetricDataInfo, error)
}

type metricClient struct {
	cc grpc.ClientConnInterface
}

func NewMetricClient(cc grpc.ClientConnInterface) MetricClient {
	return &metricClient{cc}
}

func (c *metricClient) List(ctx context.Context, in *MetricRequest, opts ...grpc.CallOption) (*MetricsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(MetricsInfo)
	err := c.cc.Invoke(ctx, Metric_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *metricClient) GetData(ctx context.Context, in *MetricDataRequest, opts ...grpc.CallOption) (*MetricDataInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(MetricDataInfo)
	err := c.cc.Invoke(ctx, Metric_GetData_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MetricServer is the server API for Metric service.
// All implementations must embed UnimplementedMetricServer
// for forward compatibility
type MetricServer interface {
	// Gets a list of all Metrics from a specific cloud service. You can use the method to list up the Metrics to collect before using the `get_data` method to collect the Metrics.
	List(context.Context, *MetricRequest) (*MetricsInfo, error)
	// Gets a Metric from a specific cloud service resource `instance`. By specifying the time period to collect the Metric, the Metric data value of the `instance` during the period is returned.
	GetData(context.Context, *MetricDataRequest) (*MetricDataInfo, error)
	mustEmbedUnimplementedMetricServer()
}

// UnimplementedMetricServer must be embedded to have forward compatible implementations.
type UnimplementedMetricServer struct {
}

func (UnimplementedMetricServer) List(context.Context, *MetricRequest) (*MetricsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedMetricServer) GetData(context.Context, *MetricDataRequest) (*MetricDataInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetData not implemented")
}
func (UnimplementedMetricServer) mustEmbedUnimplementedMetricServer() {}

// UnsafeMetricServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to MetricServer will
// result in compilation errors.
type UnsafeMetricServer interface {
	mustEmbedUnimplementedMetricServer()
}

func RegisterMetricServer(s grpc.ServiceRegistrar, srv MetricServer) {
	s.RegisterService(&Metric_ServiceDesc, srv)
}

func _Metric_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MetricServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Metric_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MetricServer).List(ctx, req.(*MetricRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Metric_GetData_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricDataRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MetricServer).GetData(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Metric_GetData_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MetricServer).GetData(ctx, req.(*MetricDataRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Metric_ServiceDesc is the grpc.ServiceDesc for Metric service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Metric_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.monitoring.plugin.Metric",
	HandlerType: (*MetricServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "list",
			Handler:    _Metric_List_Handler,
		},
		{
			MethodName: "get_data",
			Handler:    _Metric_GetData_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/monitoring/plugin/metric.proto",
}
