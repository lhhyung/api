// description of dashboard

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/dashboard/v1/public_folder.proto

package v1

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
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
	PublicFolder_Create_FullMethodName = "/spaceone.api.dashboard.v1.PublicFolder/create"
	PublicFolder_Update_FullMethodName = "/spaceone.api.dashboard.v1.PublicFolder/update"
	PublicFolder_Delete_FullMethodName = "/spaceone.api.dashboard.v1.PublicFolder/delete"
	PublicFolder_Get_FullMethodName    = "/spaceone.api.dashboard.v1.PublicFolder/get"
	PublicFolder_List_FullMethodName   = "/spaceone.api.dashboard.v1.PublicFolder/list"
	PublicFolder_Stat_FullMethodName   = "/spaceone.api.dashboard.v1.PublicFolder/stat"
)

// PublicFolderClient is the client API for PublicFolder service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PublicFolderClient interface {
	Create(ctx context.Context, in *CreatePublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error)
	Update(ctx context.Context, in *UpdatePublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error)
	Delete(ctx context.Context, in *PublicFolderRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Get(ctx context.Context, in *PublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error)
	List(ctx context.Context, in *PublicFolderQuery, opts ...grpc.CallOption) (*PublicFoldersInfo, error)
	Stat(ctx context.Context, in *PublicFolderStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type publicFolderClient struct {
	cc grpc.ClientConnInterface
}

func NewPublicFolderClient(cc grpc.ClientConnInterface) PublicFolderClient {
	return &publicFolderClient{cc}
}

func (c *publicFolderClient) Create(ctx context.Context, in *CreatePublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PublicFolderInfo)
	err := c.cc.Invoke(ctx, PublicFolder_Create_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicFolderClient) Update(ctx context.Context, in *UpdatePublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PublicFolderInfo)
	err := c.cc.Invoke(ctx, PublicFolder_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicFolderClient) Delete(ctx context.Context, in *PublicFolderRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, PublicFolder_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicFolderClient) Get(ctx context.Context, in *PublicFolderRequest, opts ...grpc.CallOption) (*PublicFolderInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PublicFolderInfo)
	err := c.cc.Invoke(ctx, PublicFolder_Get_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicFolderClient) List(ctx context.Context, in *PublicFolderQuery, opts ...grpc.CallOption) (*PublicFoldersInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PublicFoldersInfo)
	err := c.cc.Invoke(ctx, PublicFolder_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicFolderClient) Stat(ctx context.Context, in *PublicFolderStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, PublicFolder_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PublicFolderServer is the server API for PublicFolder service.
// All implementations must embed UnimplementedPublicFolderServer
// for forward compatibility
type PublicFolderServer interface {
	Create(context.Context, *CreatePublicFolderRequest) (*PublicFolderInfo, error)
	Update(context.Context, *UpdatePublicFolderRequest) (*PublicFolderInfo, error)
	Delete(context.Context, *PublicFolderRequest) (*empty.Empty, error)
	Get(context.Context, *PublicFolderRequest) (*PublicFolderInfo, error)
	List(context.Context, *PublicFolderQuery) (*PublicFoldersInfo, error)
	Stat(context.Context, *PublicFolderStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedPublicFolderServer()
}

// UnimplementedPublicFolderServer must be embedded to have forward compatible implementations.
type UnimplementedPublicFolderServer struct {
}

func (UnimplementedPublicFolderServer) Create(context.Context, *CreatePublicFolderRequest) (*PublicFolderInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedPublicFolderServer) Update(context.Context, *UpdatePublicFolderRequest) (*PublicFolderInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedPublicFolderServer) Delete(context.Context, *PublicFolderRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedPublicFolderServer) Get(context.Context, *PublicFolderRequest) (*PublicFolderInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedPublicFolderServer) List(context.Context, *PublicFolderQuery) (*PublicFoldersInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedPublicFolderServer) Stat(context.Context, *PublicFolderStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedPublicFolderServer) mustEmbedUnimplementedPublicFolderServer() {}

// UnsafePublicFolderServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PublicFolderServer will
// result in compilation errors.
type UnsafePublicFolderServer interface {
	mustEmbedUnimplementedPublicFolderServer()
}

func RegisterPublicFolderServer(s grpc.ServiceRegistrar, srv PublicFolderServer) {
	s.RegisterService(&PublicFolder_ServiceDesc, srv)
}

func _PublicFolder_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreatePublicFolderRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).Create(ctx, req.(*CreatePublicFolderRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicFolder_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdatePublicFolderRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).Update(ctx, req.(*UpdatePublicFolderRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicFolder_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicFolderRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).Delete(ctx, req.(*PublicFolderRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicFolder_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicFolderRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).Get(ctx, req.(*PublicFolderRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicFolder_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicFolderQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).List(ctx, req.(*PublicFolderQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicFolder_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicFolderStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicFolderServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicFolder_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicFolderServer).Stat(ctx, req.(*PublicFolderStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// PublicFolder_ServiceDesc is the grpc.ServiceDesc for PublicFolder service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PublicFolder_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.dashboard.v1.PublicFolder",
	HandlerType: (*PublicFolderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _PublicFolder_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _PublicFolder_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _PublicFolder_Delete_Handler,
		},
		{
			MethodName: "get",
			Handler:    _PublicFolder_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _PublicFolder_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _PublicFolder_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/dashboard/v1/public_folder.proto",
}
