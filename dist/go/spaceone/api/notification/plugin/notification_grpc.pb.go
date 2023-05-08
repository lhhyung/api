//
//desc: A Notification is a resource delivering data from a Protocol plugin instance to a nofitication tool of an external user.

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.6.1
// source: spaceone/api/notification/plugin/notification.proto

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
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	Notification_Dispatch_FullMethodName = "/spaceone.api.notification.plugin.Notification/dispatch"
)

// NotificationClient is the client API for Notification service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type NotificationClient interface {
	// desc: Dispatches data from Cloudforet to a specific notification Protocol. When dispatching data, data input by a User is included in the `options` parameter, and `notification` information to be delivered is included in the `message` parameter. Also, data dispatched includes basic information such as `notification_type` and `secret_data`.
	// request_example: >-
	// {
	// "options": {},
	// "message": {
	// "tags": [
	// {
	// "key": "Alert Number",
	// "options": {"short": true},
	// "value": "#108664"
	// },
	// {
	// "options": {"short": true},
	// "key": "State",
	// "value": "TRIGGERED"
	// },
	// {
	// "value": "LOW",
	// "options": {"short": true},
	// "key": "Urgency"
	// },
	// {
	// "value": "kubectl-webhook",
	// "key": "Triggered by",
	// "options": {"short": true}
	// },
	// {
	// "value": "SpaceONE > Project1",
	// "key": "Project"
	// },
	// {
	// "value": "spaceone-api",
	// "key": "Resource"
	// }
	// ],
	// "occurred_at": "2022-06-27T09:22:57.967Z",
	// "callbacks": [{
	// "url": "https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-x1v2c3v456/8f2ede36213dqw4d7d5awe07ds32d883/ACKNOWLEDGED",
	// "label": "Acknowledge Alerts"}],
	// "link": "https://spaceone.console.dev.spaceone.dev/alert-manager/alert/alert-x1v2c3v456",
	// "title": "[Alerting] Notification of access to the SpaceONE",
	// "description": "SSH Access to spaceone-api from admin"},
	// "notification_type": "INFO",
	// "secret_data": "********",
	// "channel_data": {"email": "test5@test.com"}
	// }
	Dispatch(ctx context.Context, in *PluginDispatchRequest, opts ...grpc.CallOption) (*empty.Empty, error)
}

type notificationClient struct {
	cc grpc.ClientConnInterface
}

func NewNotificationClient(cc grpc.ClientConnInterface) NotificationClient {
	return &notificationClient{cc}
}

func (c *notificationClient) Dispatch(ctx context.Context, in *PluginDispatchRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, Notification_Dispatch_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// NotificationServer is the server API for Notification service.
// All implementations must embed UnimplementedNotificationServer
// for forward compatibility
type NotificationServer interface {
	// desc: Dispatches data from Cloudforet to a specific notification Protocol. When dispatching data, data input by a User is included in the `options` parameter, and `notification` information to be delivered is included in the `message` parameter. Also, data dispatched includes basic information such as `notification_type` and `secret_data`.
	// request_example: >-
	// {
	// "options": {},
	// "message": {
	// "tags": [
	// {
	// "key": "Alert Number",
	// "options": {"short": true},
	// "value": "#108664"
	// },
	// {
	// "options": {"short": true},
	// "key": "State",
	// "value": "TRIGGERED"
	// },
	// {
	// "value": "LOW",
	// "options": {"short": true},
	// "key": "Urgency"
	// },
	// {
	// "value": "kubectl-webhook",
	// "key": "Triggered by",
	// "options": {"short": true}
	// },
	// {
	// "value": "SpaceONE > Project1",
	// "key": "Project"
	// },
	// {
	// "value": "spaceone-api",
	// "key": "Resource"
	// }
	// ],
	// "occurred_at": "2022-06-27T09:22:57.967Z",
	// "callbacks": [{
	// "url": "https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-x1v2c3v456/8f2ede36213dqw4d7d5awe07ds32d883/ACKNOWLEDGED",
	// "label": "Acknowledge Alerts"}],
	// "link": "https://spaceone.console.dev.spaceone.dev/alert-manager/alert/alert-x1v2c3v456",
	// "title": "[Alerting] Notification of access to the SpaceONE",
	// "description": "SSH Access to spaceone-api from admin"},
	// "notification_type": "INFO",
	// "secret_data": "********",
	// "channel_data": {"email": "test5@test.com"}
	// }
	Dispatch(context.Context, *PluginDispatchRequest) (*empty.Empty, error)
	mustEmbedUnimplementedNotificationServer()
}

// UnimplementedNotificationServer must be embedded to have forward compatible implementations.
type UnimplementedNotificationServer struct {
}

func (UnimplementedNotificationServer) Dispatch(context.Context, *PluginDispatchRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Dispatch not implemented")
}
func (UnimplementedNotificationServer) mustEmbedUnimplementedNotificationServer() {}

// UnsafeNotificationServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to NotificationServer will
// result in compilation errors.
type UnsafeNotificationServer interface {
	mustEmbedUnimplementedNotificationServer()
}

func RegisterNotificationServer(s grpc.ServiceRegistrar, srv NotificationServer) {
	s.RegisterService(&Notification_ServiceDesc, srv)
}

func _Notification_Dispatch_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PluginDispatchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NotificationServer).Dispatch(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Notification_Dispatch_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NotificationServer).Dispatch(ctx, req.(*PluginDispatchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Notification_ServiceDesc is the grpc.ServiceDesc for Notification service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Notification_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.notification.plugin.Notification",
	HandlerType: (*NotificationServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "dispatch",
			Handler:    _Notification_Dispatch_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/notification/plugin/notification.proto",
}