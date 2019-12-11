# requries
go >=1.6

# install grpc 
```
go get -u google.golang.org/grpc
```

# Install Protocol Buffers v3
download protoc
```
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.11.1/protoc-3.11.1-linux-x86_64.zip
unzip protoc-3.11.1-linux-x86_64.zip
cp bin/protoc /usr/local/bin/
```

# install the protoc plugin for go
```
go get -u github.com/golang/protobuf/protoc-gen-go
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

# generate go code
```
protoc -I=../protos --go_out=plugins=grpc:. hello.proto
```
one file generated hello.pb.go

# write application client and server
```
project dir
├── client
│   ├── go.mod
│   ├── go.sum
│   ├── hello.pb.go
│   └── main.go
└── server
    ├── go.mod
    ├── go.sum
    ├── hello.pb.go
    └── main.go
```

client/main.go
```go
package main

import (
        "context"
        "fmt"
        "log"

        "google.golang.org/grpc"


)

func main() {
        conn, err := grpc.Dial("localhost:1234", grpc.WithInsecure())
        if err != nil {
                log.Fatal(err)
        }
        defer conn.Close()

        client := NewHelloServiceClient(conn)
        reply, err := client.Hello(context.Background(), &String{Value: "hello"})
        if err != nil {
                log.Fatal(err)
        }

        fmt.Println(reply.GetValue())
}
```

server/main.go
```go
package main

import (
        "context"
        "log"
        "net"

        "google.golang.org/grpc"
        "google.golang.org/grpc/reflection"
)

type HelloServiceImpl struct{}

func (p *HelloServiceImpl) Hello(
        ctx context.Context, args *String,
) (*String, error) {
        reply := &String{Value: "hello:" + args.GetValue()}
        return reply, nil
}

func main() {
        grpcServer := grpc.NewServer()
        RegisterHelloServiceServer(grpcServer, new(HelloServiceImpl))

        lis, err := net.Listen("tcp", ":1234")
        if err != nil {
                log.Fatal(err)
        }
        reflection.Register(grpcServer)
        grpcServer.Serve(lis)
}
```

## run
Run the server
```shell
cd server && go run .
```
run the client
```shell
cd client && go run .
```






