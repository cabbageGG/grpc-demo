from concurrent import futures
import logging

import grpc

import hello_pb2
import hello_pb2_grpc


class HelloService(hello_pb2_grpc.HelloServiceServicer):

    def Hello(self, request, context):
        return hello_pb2.String(value='Hello, %s!' % request.value)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:1234')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

