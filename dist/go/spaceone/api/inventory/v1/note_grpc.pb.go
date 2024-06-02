// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v3.6.1
// source: spaceone/api/inventory/v1/note.proto

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
	Note_Create_FullMethodName = "/spaceone.api.inventory.v1.Note/create"
	Note_Update_FullMethodName = "/spaceone.api.inventory.v1.Note/update"
	Note_Delete_FullMethodName = "/spaceone.api.inventory.v1.Note/delete"
	Note_Get_FullMethodName    = "/spaceone.api.inventory.v1.Note/get"
	Note_List_FullMethodName   = "/spaceone.api.inventory.v1.Note/list"
	Note_Stat_FullMethodName   = "/spaceone.api.inventory.v1.Note/stat"
)

// NoteClient is the client API for Note service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type NoteClient interface {
	Create(ctx context.Context, in *CreateNoteRequest, opts ...grpc.CallOption) (*NoteInfo, error)
	Update(ctx context.Context, in *UpdateNoteRequest, opts ...grpc.CallOption) (*NoteInfo, error)
	Delete(ctx context.Context, in *NoteRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Get(ctx context.Context, in *NoteRequest, opts ...grpc.CallOption) (*NoteInfo, error)
	List(ctx context.Context, in *NoteQuery, opts ...grpc.CallOption) (*NotesInfo, error)
	Stat(ctx context.Context, in *NoteStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type noteClient struct {
	cc grpc.ClientConnInterface
}

func NewNoteClient(cc grpc.ClientConnInterface) NoteClient {
	return &noteClient{cc}
}

func (c *noteClient) Create(ctx context.Context, in *CreateNoteRequest, opts ...grpc.CallOption) (*NoteInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(NoteInfo)
	err := c.cc.Invoke(ctx, Note_Create_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *noteClient) Update(ctx context.Context, in *UpdateNoteRequest, opts ...grpc.CallOption) (*NoteInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(NoteInfo)
	err := c.cc.Invoke(ctx, Note_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *noteClient) Delete(ctx context.Context, in *NoteRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, Note_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *noteClient) Get(ctx context.Context, in *NoteRequest, opts ...grpc.CallOption) (*NoteInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(NoteInfo)
	err := c.cc.Invoke(ctx, Note_Get_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *noteClient) List(ctx context.Context, in *NoteQuery, opts ...grpc.CallOption) (*NotesInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(NotesInfo)
	err := c.cc.Invoke(ctx, Note_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *noteClient) Stat(ctx context.Context, in *NoteStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, Note_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// NoteServer is the server API for Note service.
// All implementations must embed UnimplementedNoteServer
// for forward compatibility
type NoteServer interface {
	Create(context.Context, *CreateNoteRequest) (*NoteInfo, error)
	Update(context.Context, *UpdateNoteRequest) (*NoteInfo, error)
	Delete(context.Context, *NoteRequest) (*empty.Empty, error)
	Get(context.Context, *NoteRequest) (*NoteInfo, error)
	List(context.Context, *NoteQuery) (*NotesInfo, error)
	Stat(context.Context, *NoteStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedNoteServer()
}

// UnimplementedNoteServer must be embedded to have forward compatible implementations.
type UnimplementedNoteServer struct {
}

func (UnimplementedNoteServer) Create(context.Context, *CreateNoteRequest) (*NoteInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedNoteServer) Update(context.Context, *UpdateNoteRequest) (*NoteInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedNoteServer) Delete(context.Context, *NoteRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedNoteServer) Get(context.Context, *NoteRequest) (*NoteInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedNoteServer) List(context.Context, *NoteQuery) (*NotesInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedNoteServer) Stat(context.Context, *NoteStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedNoteServer) mustEmbedUnimplementedNoteServer() {}

// UnsafeNoteServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to NoteServer will
// result in compilation errors.
type UnsafeNoteServer interface {
	mustEmbedUnimplementedNoteServer()
}

func RegisterNoteServer(s grpc.ServiceRegistrar, srv NoteServer) {
	s.RegisterService(&Note_ServiceDesc, srv)
}

func _Note_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateNoteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).Create(ctx, req.(*CreateNoteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Note_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateNoteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).Update(ctx, req.(*UpdateNoteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Note_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NoteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).Delete(ctx, req.(*NoteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Note_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NoteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).Get(ctx, req.(*NoteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Note_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NoteQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).List(ctx, req.(*NoteQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _Note_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NoteStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NoteServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Note_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NoteServer).Stat(ctx, req.(*NoteStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// Note_ServiceDesc is the grpc.ServiceDesc for Note service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Note_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.inventory.v1.Note",
	HandlerType: (*NoteServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _Note_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _Note_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _Note_Delete_Handler,
		},
		{
			MethodName: "get",
			Handler:    _Note_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _Note_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _Note_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/inventory/v1/note.proto",
}
