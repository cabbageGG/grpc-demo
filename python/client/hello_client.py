from __future__ import print_function
import logging

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:1234') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        response = stub.Hello(hello_pb2.String(value='you'))
        print("Hello Service client received: " + response.value)



if __name__ == '__main__':
    logging.basicConfig()
    run()

