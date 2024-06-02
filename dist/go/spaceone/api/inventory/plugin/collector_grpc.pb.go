// A Collector is a plugin collecting data of external infrastructure resources.

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/inventory/plugin/collector.proto

package plugin

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.62.0 or later.
const _ = grpc.SupportPackageIsVersion8

const (
	Collector_Init_FullMethodName    = "/spaceone.api.inventory.plugin.Collector/init"
	Collector_Verify_FullMethodName  = "/spaceone.api.inventory.plugin.Collector/verify"
	Collector_Collect_FullMethodName = "/spaceone.api.inventory.plugin.Collector/collect"
)

// CollectorClient is the client API for Collector service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type CollectorClient interface {
	// Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.
	Init(ctx context.Context, in *InitRequest, opts ...grpc.CallOption) (*PluginInfo, error)
	// Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.
	Verify(ctx context.Context, in *VerifyRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	// Collects data of external infrastructure resources by a specific Collector.
	Collect(ctx context.Context, in *CollectRequest, opts ...grpc.CallOption) (Collector_CollectClient, error)
}

type collectorClient struct {
	cc grpc.ClientConnInterface
}

func NewCollectorClient(cc grpc.ClientConnInterface) CollectorClient {
	return &collectorClient{cc}
}

func (c *collectorClient) Init(ctx context.Context, in *InitRequest, opts ...grpc.CallOption) (*PluginInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PluginInfo)
	err := c.cc.Invoke(ctx, Collector_Init_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *collectorClient) Verify(ctx context.Context, in *VerifyRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, Collector_Verify_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *collectorClient) Collect(ctx context.Context, in *CollectRequest, opts ...grpc.CallOption) (Collector_CollectClient, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &Collector_ServiceDesc.Streams[0], Collector_Collect_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &collectorCollectClient{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Collector_CollectClient interface {
	Recv() (*ResourceInfo, error)
	grpc.ClientStream
}

type collectorCollectClient struct {
	grpc.ClientStream
}

func (x *collectorCollectClient) Recv() (*ResourceInfo, error) {
	m := new(ResourceInfo)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// CollectorServer is the server API for Collector service.
// All implementations must embed UnimplementedCollectorServer
// for forward compatibility
type CollectorServer interface {
	// Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.
	Init(context.Context, *InitRequest) (*PluginInfo, error)
	// Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.
	Verify(context.Context, *VerifyRequest) (*empty.Empty, error)
	// Collects data of external infrastructure resources by a specific Collector.
	Collect(*CollectRequest, Collector_CollectServer) error
	mustEmbedUnimplementedCollectorServer()
}

// UnimplementedCollectorServer must be embedded to have forward compatible implementations.
type UnimplementedCollectorServer struct {
}

func (UnimplementedCollectorServer) Init(context.Context, *InitRequest) (*PluginInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Init not implemented")
}
func (UnimplementedCollectorServer) Verify(context.Context, *VerifyRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Verify not implemented")
}
func (UnimplementedCollectorServer) Collect(*CollectRequest, Collector_CollectServer) error {
	return status.Errorf(codes.Unimplemented, "method Collect not implemented")
}
func (UnimplementedCollectorServer) mustEmbedUnimplementedCollectorServer() {}

// UnsafeCollectorServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to CollectorServer will
// result in compilation errors.
type UnsafeCollectorServer interface {
	mustEmbedUnimplementedCollectorServer()
}

func RegisterCollectorServer(s grpc.ServiceRegistrar, srv CollectorServer) {
	s.RegisterService(&Collector_ServiceDesc, srv)
}

func _Collector_Init_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CollectorServer).Init(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Collector_Init_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CollectorServer).Init(ctx, req.(*InitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Collector_Verify_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(VerifyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CollectorServer).Verify(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Collector_Verify_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CollectorServer).Verify(ctx, req.(*VerifyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Collector_Collect_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(CollectRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(CollectorServer).Collect(m, &collectorCollectServer{ServerStream: stream})
}

type Collector_CollectServer interface {
	Send(*ResourceInfo) error
	grpc.ServerStream
}

type collectorCollectServer struct {
	grpc.ServerStream
}

func (x *collectorCollectServer) Send(m *ResourceInfo) error {
	return x.ServerStream.SendMsg(m)
}

// Collector_ServiceDesc is the grpc.ServiceDesc for Collector service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Collector_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.inventory.plugin.Collector",
	HandlerType: (*CollectorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "init",
			Handler:    _Collector_Init_Handler,
		},
		{
			MethodName: "verify",
			Handler:    _Collector_Verify_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "collect",
			Handler:       _Collector_Collect_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "spaceone/api/inventory/plugin/collector.proto",
}
