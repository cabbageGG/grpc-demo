# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hello_pb2 as hello__pb2


class HelloServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Hello = channel.unary_unary(
        '/main.HelloService/Hello',
        request_serializer=hello__pb2.String.SerializeToString,
        response_deserializer=hello__pb2.String.FromString,
        )


class HelloServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Hello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Hello': grpc.unary_unary_rpc_method_handler(
          servicer.Hello,
          request_deserializer=hello__pb2.String.FromString,
          response_serializer=hello__pb2.String.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'main.HelloService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
