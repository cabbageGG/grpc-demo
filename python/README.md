# requries
- python >=2.7 or 3.4
- pip >= 9.0.1 
```
python -m pip install --upgrade pip
```

# install grpc
```
python -m pip install grpcio
```

# install grpc tools
```
python -m pip install grpcio-tools
```

# write protobuf 
```proto
syntax = "proto3";

package main;

message String {
	string value = 1;
}

service HelloService {
	rpc Hello (String) returns (String);
}
```

# generate python code
```
python -m grpc_tools.protoc -I=../protos --python_out=. --grpc_python_out=. hello.proto
```
two file generated hello_pb2.py, hello_pb2_grpc.py

# write application client and server
```
project dir
├── client
│   ├── hello_client.py
│   ├── hello_pb2_grpc.py
│   └── hello_pb2.py
└── server
    ├── hello_pb2_grpc.py
    ├── hello_pb2.py
    └── hello_server.py
```

hello_client.py
```python
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
```
hello_server.py
```python
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
```

## run
Run the server
```shell
cd server && python hello_server.py
```
run the client
```shell
cd client && python hello_client.py
```






