# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/protobuf/xplane.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/protobuf/xplane.proto',
  package='tensorflow.profiler',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n.tensorflow/core/profiler/protobuf/xplane.proto\x12\x13tensorflow.profiler\"W\n\x06XSpace\x12+\n\x06planes\x18\x01 \x03(\x0b\x32\x1b.tensorflow.profiler.XPlane\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t\x12\x10\n\x08warnings\x18\x03 \x03(\t\"\xba\x03\n\x06XPlane\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x05lines\x18\x03 \x03(\x0b\x32\x1a.tensorflow.profiler.XLine\x12\x46\n\x0e\x65vent_metadata\x18\x04 \x03(\x0b\x32..tensorflow.profiler.XPlane.EventMetadataEntry\x12\x44\n\rstat_metadata\x18\x05 \x03(\x0b\x32-.tensorflow.profiler.XPlane.StatMetadataEntry\x12)\n\x05stats\x18\x06 \x03(\x0b\x32\x1a.tensorflow.profiler.XStat\x1aY\n\x12\x45ventMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.tensorflow.profiler.XEventMetadata:\x02\x38\x01\x1aW\n\x11StatMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".tensorflow.profiler.XStatMetadata:\x02\x38\x01\"\xbb\x01\n\x05XLine\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\ndisplay_id\x18\n \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x0b \x01(\t\x12\x14\n\x0ctimestamp_ns\x18\x03 \x01(\x03\x12\x13\n\x0b\x64uration_ps\x18\t \x01(\x03\x12+\n\x06\x65vents\x18\x04 \x03(\x0b\x32\x1b.tensorflow.profiler.XEventJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"\x95\x01\n\x06XEvent\x12\x13\n\x0bmetadata_id\x18\x01 \x01(\x03\x12\x13\n\toffset_ps\x18\x02 \x01(\x03H\x00\x12\x19\n\x0fnum_occurrences\x18\x05 \x01(\x03H\x00\x12\x13\n\x0b\x64uration_ps\x18\x03 \x01(\x03\x12)\n\x05stats\x18\x04 \x03(\x0b\x32\x1a.tensorflow.profiler.XStatB\x06\n\x04\x64\x61ta\"\xad\x01\n\x05XStat\x12\x13\n\x0bmetadata_id\x18\x01 \x01(\x03\x12\x16\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cuint64_value\x18\x03 \x01(\x04H\x00\x12\x15\n\x0bint64_value\x18\x04 \x01(\x03H\x00\x12\x13\n\tstr_value\x18\x05 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x06 \x01(\x0cH\x00\x12\x13\n\tref_value\x18\x07 \x01(\x04H\x00\x42\x07\n\x05value\"R\n\x0eXEventMetadata\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\x0c\">\n\rXStatMetadata\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x03\xf8\x01\x01\x62\x06proto3')
)




_XSPACE = _descriptor.Descriptor(
  name='XSpace',
  full_name='tensorflow.profiler.XSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='planes', full_name='tensorflow.profiler.XSpace.planes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='tensorflow.profiler.XSpace.errors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warnings', full_name='tensorflow.profiler.XSpace.warnings', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=71,
  serialized_end=158,
)


_XPLANE_EVENTMETADATAENTRY = _descriptor.Descriptor(
  name='EventMetadataEntry',
  full_name='tensorflow.profiler.XPlane.EventMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.profiler.XPlane.EventMetadataEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.profiler.XPlane.EventMetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=514,
)

_XPLANE_STATMETADATAENTRY = _descriptor.Descriptor(
  name='StatMetadataEntry',
  full_name='tensorflow.profiler.XPlane.StatMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.profiler.XPlane.StatMetadataEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.profiler.XPlane.StatMetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=603,
)

_XPLANE = _descriptor.Descriptor(
  name='XPlane',
  full_name='tensorflow.profiler.XPlane',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.profiler.XPlane.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.profiler.XPlane.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines', full_name='tensorflow.profiler.XPlane.lines', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_metadata', full_name='tensorflow.profiler.XPlane.event_metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat_metadata', full_name='tensorflow.profiler.XPlane.stat_metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='tensorflow.profiler.XPlane.stats', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_XPLANE_EVENTMETADATAENTRY, _XPLANE_STATMETADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=603,
)


_XLINE = _descriptor.Descriptor(
  name='XLine',
  full_name='tensorflow.profiler.XLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.profiler.XLine.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_id', full_name='tensorflow.profiler.XLine.display_id', index=1,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.profiler.XLine.name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='tensorflow.profiler.XLine.display_name', index=3,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_ns', full_name='tensorflow.profiler.XLine.timestamp_ns', index=4,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_ps', full_name='tensorflow.profiler.XLine.duration_ps', index=5,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='tensorflow.profiler.XLine.events', index=6,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=606,
  serialized_end=793,
)


_XEVENT = _descriptor.Descriptor(
  name='XEvent',
  full_name='tensorflow.profiler.XEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata_id', full_name='tensorflow.profiler.XEvent.metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_ps', full_name='tensorflow.profiler.XEvent.offset_ps', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_occurrences', full_name='tensorflow.profiler.XEvent.num_occurrences', index=2,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_ps', full_name='tensorflow.profiler.XEvent.duration_ps', index=3,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='tensorflow.profiler.XEvent.stats', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='data', full_name='tensorflow.profiler.XEvent.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=796,
  serialized_end=945,
)


_XSTAT = _descriptor.Descriptor(
  name='XStat',
  full_name='tensorflow.profiler.XStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata_id', full_name='tensorflow.profiler.XStat.metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='tensorflow.profiler.XStat.double_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='tensorflow.profiler.XStat.uint64_value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='tensorflow.profiler.XStat.int64_value', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_value', full_name='tensorflow.profiler.XStat.str_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='tensorflow.profiler.XStat.bytes_value', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_value', full_name='tensorflow.profiler.XStat.ref_value', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='tensorflow.profiler.XStat.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=948,
  serialized_end=1121,
)


_XEVENTMETADATA = _descriptor.Descriptor(
  name='XEventMetadata',
  full_name='tensorflow.profiler.XEventMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.profiler.XEventMetadata.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.profiler.XEventMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='tensorflow.profiler.XEventMetadata.display_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow.profiler.XEventMetadata.metadata', index=3,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1123,
  serialized_end=1205,
)


_XSTATMETADATA = _descriptor.Descriptor(
  name='XStatMetadata',
  full_name='tensorflow.profiler.XStatMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.profiler.XStatMetadata.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.profiler.XStatMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.profiler.XStatMetadata.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1207,
  serialized_end=1269,
)

_XSPACE.fields_by_name['planes'].message_type = _XPLANE
_XPLANE_EVENTMETADATAENTRY.fields_by_name['value'].message_type = _XEVENTMETADATA
_XPLANE_EVENTMETADATAENTRY.containing_type = _XPLANE
_XPLANE_STATMETADATAENTRY.fields_by_name['value'].message_type = _XSTATMETADATA
_XPLANE_STATMETADATAENTRY.containing_type = _XPLANE
_XPLANE.fields_by_name['lines'].message_type = _XLINE
_XPLANE.fields_by_name['event_metadata'].message_type = _XPLANE_EVENTMETADATAENTRY
_XPLANE.fields_by_name['stat_metadata'].message_type = _XPLANE_STATMETADATAENTRY
_XPLANE.fields_by_name['stats'].message_type = _XSTAT
_XLINE.fields_by_name['events'].message_type = _XEVENT
_XEVENT.fields_by_name['stats'].message_type = _XSTAT
_XEVENT.oneofs_by_name['data'].fields.append(
  _XEVENT.fields_by_name['offset_ps'])
_XEVENT.fields_by_name['offset_ps'].containing_oneof = _XEVENT.oneofs_by_name['data']
_XEVENT.oneofs_by_name['data'].fields.append(
  _XEVENT.fields_by_name['num_occurrences'])
_XEVENT.fields_by_name['num_occurrences'].containing_oneof = _XEVENT.oneofs_by_name['data']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['double_value'])
_XSTAT.fields_by_name['double_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['uint64_value'])
_XSTAT.fields_by_name['uint64_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['int64_value'])
_XSTAT.fields_by_name['int64_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['str_value'])
_XSTAT.fields_by_name['str_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['bytes_value'])
_XSTAT.fields_by_name['bytes_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
_XSTAT.oneofs_by_name['value'].fields.append(
  _XSTAT.fields_by_name['ref_value'])
_XSTAT.fields_by_name['ref_value'].containing_oneof = _XSTAT.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['XSpace'] = _XSPACE
DESCRIPTOR.message_types_by_name['XPlane'] = _XPLANE
DESCRIPTOR.message_types_by_name['XLine'] = _XLINE
DESCRIPTOR.message_types_by_name['XEvent'] = _XEVENT
DESCRIPTOR.message_types_by_name['XStat'] = _XSTAT
DESCRIPTOR.message_types_by_name['XEventMetadata'] = _XEVENTMETADATA
DESCRIPTOR.message_types_by_name['XStatMetadata'] = _XSTATMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XSpace = _reflection.GeneratedProtocolMessageType('XSpace', (_message.Message,), {
  'DESCRIPTOR' : _XSPACE,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XSpace)
  })
_sym_db.RegisterMessage(XSpace)

XPlane = _reflection.GeneratedProtocolMessageType('XPlane', (_message.Message,), {

  'EventMetadataEntry' : _reflection.GeneratedProtocolMessageType('EventMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _XPLANE_EVENTMETADATAENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.XPlane.EventMetadataEntry)
    })
  ,

  'StatMetadataEntry' : _reflection.GeneratedProtocolMessageType('StatMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _XPLANE_STATMETADATAENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.XPlane.StatMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _XPLANE,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XPlane)
  })
_sym_db.RegisterMessage(XPlane)
_sym_db.RegisterMessage(XPlane.EventMetadataEntry)
_sym_db.RegisterMessage(XPlane.StatMetadataEntry)

XLine = _reflection.GeneratedProtocolMessageType('XLine', (_message.Message,), {
  'DESCRIPTOR' : _XLINE,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XLine)
  })
_sym_db.RegisterMessage(XLine)

XEvent = _reflection.GeneratedProtocolMessageType('XEvent', (_message.Message,), {
  'DESCRIPTOR' : _XEVENT,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XEvent)
  })
_sym_db.RegisterMessage(XEvent)

XStat = _reflection.GeneratedProtocolMessageType('XStat', (_message.Message,), {
  'DESCRIPTOR' : _XSTAT,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XStat)
  })
_sym_db.RegisterMessage(XStat)

XEventMetadata = _reflection.GeneratedProtocolMessageType('XEventMetadata', (_message.Message,), {
  'DESCRIPTOR' : _XEVENTMETADATA,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XEventMetadata)
  })
_sym_db.RegisterMessage(XEventMetadata)

XStatMetadata = _reflection.GeneratedProtocolMessageType('XStatMetadata', (_message.Message,), {
  'DESCRIPTOR' : _XSTATMETADATA,
  '__module__' : 'tensorflow.core.profiler.protobuf.xplane_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.XStatMetadata)
  })
_sym_db.RegisterMessage(XStatMetadata)


DESCRIPTOR._options = None
_XPLANE_EVENTMETADATAENTRY._options = None
_XPLANE_STATMETADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
