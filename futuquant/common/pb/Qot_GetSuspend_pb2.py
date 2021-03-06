# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetSuspend.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetSuspend.proto',
  package='Qot_GetSuspend',
  syntax='proto2',
  serialized_pb=_b('\n\x14Qot_GetSuspend.proto\x12\x0eQot_GetSuspend\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"U\n\x03\x43\x32S\x12*\n\x0csecurityList\x18\x01 \x03(\x0b\x32\x14.Qot_Common.Security\x12\x11\n\tbeginTime\x18\x02 \x02(\t\x12\x0f\n\x07\x65ndTime\x18\x03 \x02(\t\"\x17\n\x07Suspend\x12\x0c\n\x04time\x18\x01 \x02(\t\"g\n\x0fSecuritySuspend\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12,\n\x0bsuspendList\x18\x02 \x03(\x0b\x32\x17.Qot_GetSuspend.Suspend\"C\n\x03S2C\x12<\n\x13SecuritySuspendList\x18\x01 \x03(\x0b\x32\x1f.Qot_GetSuspend.SecuritySuspend\"+\n\x07Request\x12 \n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x13.Qot_GetSuspend.C2S\"d\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12 \n\x03s2c\x18\x04 \x01(\x0b\x32\x13.Qot_GetSuspend.S2C')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetSuspend.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='securityList', full_name='Qot_GetSuspend.C2S.securityList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginTime', full_name='Qot_GetSuspend.C2S.beginTime', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='Qot_GetSuspend.C2S.endTime', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=157,
)


_SUSPEND = _descriptor.Descriptor(
  name='Suspend',
  full_name='Qot_GetSuspend.Suspend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='Qot_GetSuspend.Suspend.time', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=182,
)


_SECURITYSUSPEND = _descriptor.Descriptor(
  name='SecuritySuspend',
  full_name='Qot_GetSuspend.SecuritySuspend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetSuspend.SecuritySuspend.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspendList', full_name='Qot_GetSuspend.SecuritySuspend.suspendList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=287,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetSuspend.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SecuritySuspendList', full_name='Qot_GetSuspend.S2C.SecuritySuspendList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=356,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetSuspend.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetSuspend.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=401,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetSuspend.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetSuspend.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetSuspend.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetSuspend.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetSuspend.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=503,
)

_C2S.fields_by_name['securityList'].message_type = Qot__Common__pb2._SECURITY
_SECURITYSUSPEND.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_SECURITYSUSPEND.fields_by_name['suspendList'].message_type = _SUSPEND
_S2C.fields_by_name['SecuritySuspendList'].message_type = _SECURITYSUSPEND
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['Suspend'] = _SUSPEND
DESCRIPTOR.message_types_by_name['SecuritySuspend'] = _SECURITYSUSPEND
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.C2S)
  ))
_sym_db.RegisterMessage(C2S)

Suspend = _reflection.GeneratedProtocolMessageType('Suspend', (_message.Message,), dict(
  DESCRIPTOR = _SUSPEND,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.Suspend)
  ))
_sym_db.RegisterMessage(Suspend)

SecuritySuspend = _reflection.GeneratedProtocolMessageType('SecuritySuspend', (_message.Message,), dict(
  DESCRIPTOR = _SECURITYSUSPEND,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.SecuritySuspend)
  ))
_sym_db.RegisterMessage(SecuritySuspend)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetSuspend_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetSuspend.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
