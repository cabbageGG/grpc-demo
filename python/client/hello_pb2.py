# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='main',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bhello.proto\x12\x04main\"\x17\n\x06String\x12\r\n\x05value\x18\x01 \x01(\t23\n\x0cHelloService\x12#\n\x05Hello\x12\x0c.main.String\x1a\x0c.main.Stringb\x06proto3')
)




_STRING = _descriptor.Descriptor(
  name='String',
  full_name='main.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='main.String.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=44,
)

DESCRIPTOR.message_types_by_name['String'] = _STRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:main.String)
  })
_sym_db.RegisterMessage(String)



_HELLOSERVICE = _descriptor.ServiceDescriptor(
  name='HelloService',
  full_name='main.HelloService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=46,
  serialized_end=97,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hello',
    full_name='main.HelloService.Hello',
    index=0,
    containing_service=None,
    input_type=_STRING,
    output_type=_STRING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOSERVICE)

DESCRIPTOR.services_by_name['HelloService'] = _HELLOSERVICE

# @@protoc_insertion_point(module_scope)
