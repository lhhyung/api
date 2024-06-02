// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/identity/v2/endpoint.proto

package v2

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
	Endpoint_List_FullMethodName = "/spaceone.api.identity.v2.Endpoint/list"
)

// EndpointClient is the client API for Endpoint service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EndpointClient interface {
	// +noauth
	List(ctx context.Context, in *EndpointSearchQuery, opts ...grpc.CallOption) (*EndpointsInfo, error)
}

type endpointClient struct {
	cc grpc.ClientConnInterface
}

func NewEndpointClient(cc grpc.ClientConnInterface) EndpointClient {
	return &endpointClient{cc}
}

func (c *endpointClient) List(ctx context.Context, in *EndpointSearchQuery, opts ...grpc.CallOption) (*EndpointsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EndpointsInfo)
	err := c.cc.Invoke(ctx, Endpoint_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EndpointServer is the server API for Endpoint service.
// All implementations must embed UnimplementedEndpointServer
// for forward compatibility
type EndpointServer interface {
	// +noauth
	List(context.Context, *EndpointSearchQuery) (*EndpointsInfo, error)
	mustEmbedUnimplementedEndpointServer()
}

// UnimplementedEndpointServer must be embedded to have forward compatible implementations.
type UnimplementedEndpointServer struct {
}

func (UnimplementedEndpointServer) List(context.Context, *EndpointSearchQuery) (*EndpointsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedEndpointServer) mustEmbedUnimplementedEndpointServer() {}

// UnsafeEndpointServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EndpointServer will
// result in compilation errors.
type UnsafeEndpointServer interface {
	mustEmbedUnimplementedEndpointServer()
}

func RegisterEndpointServer(s grpc.ServiceRegistrar, srv EndpointServer) {
	s.RegisterService(&Endpoint_ServiceDesc, srv)
}

func _Endpoint_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EndpointSearchQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EndpointServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Endpoint_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EndpointServer).List(ctx, req.(*EndpointSearchQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// Endpoint_ServiceDesc is the grpc.ServiceDesc for Endpoint service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Endpoint_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.identity.v2.Endpoint",
	HandlerType: (*EndpointServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "list",
			Handler:    _Endpoint_List_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/identity/v2/endpoint.proto",
}
