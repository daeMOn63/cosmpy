# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ibc.core.channel.v1 import tx_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the ibc/channel Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChannelOpenInit = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelOpenInit',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInit.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInitResponse.FromString,
                )
        self.ChannelOpenTry = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelOpenTry',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTry.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTryResponse.FromString,
                )
        self.ChannelOpenAck = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelOpenAck',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAck.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAckResponse.FromString,
                )
        self.ChannelOpenConfirm = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelOpenConfirm',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirm.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirmResponse.FromString,
                )
        self.ChannelCloseInit = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelCloseInit',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInit.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInitResponse.FromString,
                )
        self.ChannelCloseConfirm = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/ChannelCloseConfirm',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirm.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirmResponse.FromString,
                )
        self.RecvPacket = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/RecvPacket',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacket.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacketResponse.FromString,
                )
        self.Timeout = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/Timeout',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeout.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutResponse.FromString,
                )
        self.TimeoutOnClose = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/TimeoutOnClose',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnClose.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnCloseResponse.FromString,
                )
        self.Acknowledgement = channel.unary_unary(
                '/ibc.core.channel.v1.Msg/Acknowledgement',
                request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgement.SerializeToString,
                response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgementResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the ibc/channel Msg service.
    """

    def ChannelOpenInit(self, request, context):
        """ChannelOpenInit defines a rpc handler method for MsgChannelOpenInit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelOpenTry(self, request, context):
        """ChannelOpenTry defines a rpc handler method for MsgChannelOpenTry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelOpenAck(self, request, context):
        """ChannelOpenAck defines a rpc handler method for MsgChannelOpenAck.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelOpenConfirm(self, request, context):
        """ChannelOpenConfirm defines a rpc handler method for MsgChannelOpenConfirm.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelCloseInit(self, request, context):
        """ChannelCloseInit defines a rpc handler method for MsgChannelCloseInit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelCloseConfirm(self, request, context):
        """ChannelCloseConfirm defines a rpc handler method for MsgChannelCloseConfirm.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecvPacket(self, request, context):
        """RecvPacket defines a rpc handler method for MsgRecvPacket.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Timeout(self, request, context):
        """Timeout defines a rpc handler method for MsgTimeout.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TimeoutOnClose(self, request, context):
        """TimeoutOnClose defines a rpc handler method for MsgTimeoutOnClose.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Acknowledgement(self, request, context):
        """Acknowledgement defines a rpc handler method for MsgAcknowledgement.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChannelOpenInit': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelOpenInit,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInit.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInitResponse.SerializeToString,
            ),
            'ChannelOpenTry': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelOpenTry,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTry.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTryResponse.SerializeToString,
            ),
            'ChannelOpenAck': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelOpenAck,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAck.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAckResponse.SerializeToString,
            ),
            'ChannelOpenConfirm': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelOpenConfirm,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirm.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirmResponse.SerializeToString,
            ),
            'ChannelCloseInit': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelCloseInit,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInit.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInitResponse.SerializeToString,
            ),
            'ChannelCloseConfirm': grpc.unary_unary_rpc_method_handler(
                    servicer.ChannelCloseConfirm,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirm.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirmResponse.SerializeToString,
            ),
            'RecvPacket': grpc.unary_unary_rpc_method_handler(
                    servicer.RecvPacket,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacket.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacketResponse.SerializeToString,
            ),
            'Timeout': grpc.unary_unary_rpc_method_handler(
                    servicer.Timeout,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeout.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutResponse.SerializeToString,
            ),
            'TimeoutOnClose': grpc.unary_unary_rpc_method_handler(
                    servicer.TimeoutOnClose,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnClose.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnCloseResponse.SerializeToString,
            ),
            'Acknowledgement': grpc.unary_unary_rpc_method_handler(
                    servicer.Acknowledgement,
                    request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgement.FromString,
                    response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgementResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.core.channel.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the ibc/channel Msg service.
    """

    @staticmethod
    def ChannelOpenInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelOpenInit',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInit.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelOpenTry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelOpenTry',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTry.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenTryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelOpenAck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelOpenAck',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAck.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenAckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelOpenConfirm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelOpenConfirm',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirm.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelOpenConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelCloseInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelCloseInit',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInit.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelCloseConfirm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/ChannelCloseConfirm',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirm.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgChannelCloseConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecvPacket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/RecvPacket',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacket.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgRecvPacketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Timeout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/Timeout',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeout.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TimeoutOnClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/TimeoutOnClose',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnClose.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgTimeoutOnCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Acknowledgement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Msg/Acknowledgement',
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgement.SerializeToString,
            ibc_dot_core_dot_channel_dot_v1_dot_tx__pb2.MsgAcknowledgementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
