# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/profiler_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/profiler_options.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/tensorflow/core/profiler/profiler_options.proto\x12\ntensorflow\"\xa3\x02\n\x0eProfileOptions\x12\x0f\n\x07version\x18\x05 \x01(\r\x12:\n\x0b\x64\x65vice_type\x18\x06 \x01(\x0e\x32%.tensorflow.ProfileOptions.DeviceType\x12\x1b\n\x13include_dataset_ops\x18\x01 \x01(\x08\x12\x19\n\x11host_tracer_level\x18\x02 \x01(\r\x12\x1b\n\x13\x64\x65vice_tracer_level\x18\x03 \x01(\r\x12\x1b\n\x13python_tracer_level\x18\x04 \x01(\r\x12\x18\n\x10\x65nable_hlo_proto\x18\x07 \x01(\x08\"8\n\nDeviceType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x07\n\x03\x43PU\x10\x01\x12\x07\n\x03GPU\x10\x02\x12\x07\n\x03TPU\x10\x03\x62\x06proto3')
)



_PROFILEOPTIONS_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='tensorflow.ProfileOptions.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPU', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=299,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_PROFILEOPTIONS_DEVICETYPE)


_PROFILEOPTIONS = _descriptor.Descriptor(
  name='ProfileOptions',
  full_name='tensorflow.ProfileOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.ProfileOptions.version', index=0,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='tensorflow.ProfileOptions.device_type', index=1,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_dataset_ops', full_name='tensorflow.ProfileOptions.include_dataset_ops', index=2,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_tracer_level', full_name='tensorflow.ProfileOptions.host_tracer_level', index=3,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_tracer_level', full_name='tensorflow.ProfileOptions.device_tracer_level', index=4,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python_tracer_level', full_name='tensorflow.ProfileOptions.python_tracer_level', index=5,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_hlo_proto', full_name='tensorflow.ProfileOptions.enable_hlo_proto', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROFILEOPTIONS_DEVICETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=355,
)

_PROFILEOPTIONS.fields_by_name['device_type'].enum_type = _PROFILEOPTIONS_DEVICETYPE
_PROFILEOPTIONS_DEVICETYPE.containing_type = _PROFILEOPTIONS
DESCRIPTOR.message_types_by_name['ProfileOptions'] = _PROFILEOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfileOptions = _reflection.GeneratedProtocolMessageType('ProfileOptions', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEOPTIONS,
  '__module__' : 'tensorflow.core.profiler.profiler_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ProfileOptions)
  })
_sym_db.RegisterMessage(ProfileOptions)


# @@protoc_insertion_point(module_scope)