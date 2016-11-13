# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='khero',
  syntax='proto2',
  serialized_pb=_b('\n\rmessage.proto\x12\x05khero\"\t\n\x07\x43ommand\"-\n\x07Request\x12\"\n\x05login\x18\x01 \x01(\x0b\x32\x13.khero.LoginRequest\"n\n\x08Response\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x15\n\rlast_response\x18\x02 \x02(\x08\x12\x16\n\x0e\x65rror_describe\x18\x03 \x01(\x0c\x12#\n\x05login\x18\x04 \x01(\x0b\x32\x14.khero.LoginResponse\";\n\x0cNotification\x12+\n\x07welcome\x18\x01 \x01(\x0b\x32\x1a.khero.WelcomeNotification\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x02(\x0c\x12\x10\n\x08password\x18\x02 \x02(\t\"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x02(\x07\"#\n\x13WelcomeNotification\x12\x0c\n\x04text\x18\x01 \x02(\x0c*K\n\x03Msg\x12\x13\n\rLogin_Request\x10\x81\x80\x04\x12\x14\n\x0eLogin_Response\x10\x82\x80\x04\x12\x19\n\x13Welcom_Notification\x10\x81\x80\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSG = _descriptor.EnumDescriptor(
  name='Msg',
  full_name='khero.Msg',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Login_Request', index=0, number=65537,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Login_Response', index=1, number=65538,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Welcom_Notification', index=2, number=131073,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=376,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_MSG)

Msg = enum_type_wrapper.EnumTypeWrapper(_MSG)
Login_Request = 65537
Login_Response = 65538
Welcom_Notification = 131073



_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='khero.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=24,
  serialized_end=33,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='khero.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='khero.Request.login', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=35,
  serialized_end=80,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='khero.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='khero.Response.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_response', full_name='khero.Response.last_response', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_describe', full_name='khero.Response.error_describe', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login', full_name='khero.Response.login', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=82,
  serialized_end=192,
)


_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='khero.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='welcome', full_name='khero.Notification.welcome', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=194,
  serialized_end=253,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='khero.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='khero.LoginRequest.username', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='khero.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=255,
  serialized_end=305,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='khero.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='khero.LoginResponse.token', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=307,
  serialized_end=337,
)


_WELCOMENOTIFICATION = _descriptor.Descriptor(
  name='WelcomeNotification',
  full_name='khero.WelcomeNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='khero.WelcomeNotification.text', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=339,
  serialized_end=374,
)

_REQUEST.fields_by_name['login'].message_type = _LOGINREQUEST
_RESPONSE.fields_by_name['login'].message_type = _LOGINRESPONSE
_NOTIFICATION.fields_by_name['welcome'].message_type = _WELCOMENOTIFICATION
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['WelcomeNotification'] = _WELCOMENOTIFICATION
DESCRIPTOR.enum_types_by_name['Msg'] = _MSG

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.Command)
  ))
_sym_db.RegisterMessage(Command)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.Response)
  ))
_sym_db.RegisterMessage(Response)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATION,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.Notification)
  ))
_sym_db.RegisterMessage(Notification)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.LoginRequest)
  ))
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.LoginResponse)
  ))
_sym_db.RegisterMessage(LoginResponse)

WelcomeNotification = _reflection.GeneratedProtocolMessageType('WelcomeNotification', (_message.Message,), dict(
  DESCRIPTOR = _WELCOMENOTIFICATION,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:khero.WelcomeNotification)
  ))
_sym_db.RegisterMessage(WelcomeNotification)


# @@protoc_insertion_point(module_scope)
