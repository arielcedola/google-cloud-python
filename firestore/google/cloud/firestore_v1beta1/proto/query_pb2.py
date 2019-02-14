# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/firestore_v1beta1/proto/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.firestore_v1beta1.proto import document_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/firestore_v1beta1/proto/query.proto',
  package='google.firestore.v1beta1',
  syntax='proto3',
  serialized_options=_b('\n\034com.google.firestore.v1beta1B\nQueryProtoP\001ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\242\002\004GCFS\252\002\036Google.Cloud.Firestore.V1Beta1\312\002\036Google\\Cloud\\Firestore\\V1beta1'),
  serialized_pb=_b('\n0google/cloud/firestore_v1beta1/proto/query.proto\x12\x18google.firestore.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x33google/cloud/firestore_v1beta1/proto/document.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb9\x0f\n\x0fStructuredQuery\x12\x44\n\x06select\x18\x01 \x01(\x0b\x32\x34.google.firestore.v1beta1.StructuredQuery.Projection\x12J\n\x04\x66rom\x18\x02 \x03(\x0b\x32<.google.firestore.v1beta1.StructuredQuery.CollectionSelector\x12?\n\x05where\x18\x03 \x01(\x0b\x32\x30.google.firestore.v1beta1.StructuredQuery.Filter\x12\x41\n\x08order_by\x18\x04 \x03(\x0b\x32/.google.firestore.v1beta1.StructuredQuery.Order\x12\x32\n\x08start_at\x18\x07 \x01(\x0b\x32 .google.firestore.v1beta1.Cursor\x12\x30\n\x06\x65nd_at\x18\x08 \x01(\x0b\x32 .google.firestore.v1beta1.Cursor\x12\x0e\n\x06offset\x18\x06 \x01(\x05\x12*\n\x05limit\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x1a\x44\n\x12\x43ollectionSelector\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12\x17\n\x0f\x61ll_descendants\x18\x03 \x01(\x08\x1a\x8c\x02\n\x06\x46ilter\x12U\n\x10\x63omposite_filter\x18\x01 \x01(\x0b\x32\x39.google.firestore.v1beta1.StructuredQuery.CompositeFilterH\x00\x12M\n\x0c\x66ield_filter\x18\x02 \x01(\x0b\x32\x35.google.firestore.v1beta1.StructuredQuery.FieldFilterH\x00\x12M\n\x0cunary_filter\x18\x03 \x01(\x0b\x32\x35.google.firestore.v1beta1.StructuredQuery.UnaryFilterH\x00\x42\r\n\x0b\x66ilter_type\x1a\xd3\x01\n\x0f\x43ompositeFilter\x12N\n\x02op\x18\x01 \x01(\x0e\x32\x42.google.firestore.v1beta1.StructuredQuery.CompositeFilter.Operator\x12\x41\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x30.google.firestore.v1beta1.StructuredQuery.Filter\"-\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41ND\x10\x01\x1a\xec\x02\n\x0b\x46ieldFilter\x12G\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x38.google.firestore.v1beta1.StructuredQuery.FieldReference\x12J\n\x02op\x18\x02 \x01(\x0e\x32>.google.firestore.v1beta1.StructuredQuery.FieldFilter.Operator\x12.\n\x05value\x18\x03 \x01(\x0b\x32\x1f.google.firestore.v1beta1.Value\"\x97\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05\x45QUAL\x10\x05\x12\x12\n\x0e\x41RRAY_CONTAINS\x10\x07\x1a\xf3\x01\n\x0bUnaryFilter\x12J\n\x02op\x18\x01 \x01(\x0e\x32>.google.firestore.v1beta1.StructuredQuery.UnaryFilter.Operator\x12I\n\x05\x66ield\x18\x02 \x01(\x0b\x32\x38.google.firestore.v1beta1.StructuredQuery.FieldReferenceH\x00\"=\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\n\n\x06IS_NAN\x10\x02\x12\x0b\n\x07IS_NULL\x10\x03\x42\x0e\n\x0coperand_type\x1a\x98\x01\n\x05Order\x12G\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x38.google.firestore.v1beta1.StructuredQuery.FieldReference\x12\x46\n\tdirection\x18\x02 \x01(\x0e\x32\x33.google.firestore.v1beta1.StructuredQuery.Direction\x1a$\n\x0e\x46ieldReference\x12\x12\n\nfield_path\x18\x02 \x01(\t\x1aV\n\nProjection\x12H\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x38.google.firestore.v1beta1.StructuredQuery.FieldReference\"E\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"I\n\x06\x43ursor\x12/\n\x06values\x18\x01 \x03(\x0b\x32\x1f.google.firestore.v1beta1.Value\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x01(\x08\x42\xb8\x01\n\x1c\x63om.google.firestore.v1beta1B\nQueryProtoP\x01ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])



_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='google.firestore.v1beta1.StructuredQuery.CompositeFilter.Operator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AND', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1161,
  serialized_end=1206,
)
_sym_db.RegisterEnumDescriptor(_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR)

_STRUCTUREDQUERY_FIELDFILTER_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='google.firestore.v1beta1.StructuredQuery.FieldFilter.Operator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN_OR_EQUAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN_OR_EQUAL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQUAL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARRAY_CONTAINS', index=6, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1422,
  serialized_end=1573,
)
_sym_db.RegisterEnumDescriptor(_STRUCTUREDQUERY_FIELDFILTER_OPERATOR)

_STRUCTUREDQUERY_UNARYFILTER_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='google.firestore.v1beta1.StructuredQuery.UnaryFilter.Operator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_NAN', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_NULL', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1742,
  serialized_end=1803,
)
_sym_db.RegisterEnumDescriptor(_STRUCTUREDQUERY_UNARYFILTER_OPERATOR)

_STRUCTUREDQUERY_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='google.firestore.v1beta1.StructuredQuery.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASCENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCENDING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2102,
  serialized_end=2171,
)
_sym_db.RegisterEnumDescriptor(_STRUCTUREDQUERY_DIRECTION)


_STRUCTUREDQUERY_COLLECTIONSELECTOR = _descriptor.Descriptor(
  name='CollectionSelector',
  full_name='google.firestore.v1beta1.StructuredQuery.CollectionSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_id', full_name='google.firestore.v1beta1.StructuredQuery.CollectionSelector.collection_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_descendants', full_name='google.firestore.v1beta1.StructuredQuery.CollectionSelector.all_descendants', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=653,
  serialized_end=721,
)

_STRUCTUREDQUERY_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='google.firestore.v1beta1.StructuredQuery.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='composite_filter', full_name='google.firestore.v1beta1.StructuredQuery.Filter.composite_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_filter', full_name='google.firestore.v1beta1.StructuredQuery.Filter.field_filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unary_filter', full_name='google.firestore.v1beta1.StructuredQuery.Filter.unary_filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='filter_type', full_name='google.firestore.v1beta1.StructuredQuery.Filter.filter_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=724,
  serialized_end=992,
)

_STRUCTUREDQUERY_COMPOSITEFILTER = _descriptor.Descriptor(
  name='CompositeFilter',
  full_name='google.firestore.v1beta1.StructuredQuery.CompositeFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='google.firestore.v1beta1.StructuredQuery.CompositeFilter.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='google.firestore.v1beta1.StructuredQuery.CompositeFilter.filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=995,
  serialized_end=1206,
)

_STRUCTUREDQUERY_FIELDFILTER = _descriptor.Descriptor(
  name='FieldFilter',
  full_name='google.firestore.v1beta1.StructuredQuery.FieldFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='google.firestore.v1beta1.StructuredQuery.FieldFilter.field', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='google.firestore.v1beta1.StructuredQuery.FieldFilter.op', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.firestore.v1beta1.StructuredQuery.FieldFilter.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STRUCTUREDQUERY_FIELDFILTER_OPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1209,
  serialized_end=1573,
)

_STRUCTUREDQUERY_UNARYFILTER = _descriptor.Descriptor(
  name='UnaryFilter',
  full_name='google.firestore.v1beta1.StructuredQuery.UnaryFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='google.firestore.v1beta1.StructuredQuery.UnaryFilter.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='google.firestore.v1beta1.StructuredQuery.UnaryFilter.field', index=1,
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
    _STRUCTUREDQUERY_UNARYFILTER_OPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operand_type', full_name='google.firestore.v1beta1.StructuredQuery.UnaryFilter.operand_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1576,
  serialized_end=1819,
)

_STRUCTUREDQUERY_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='google.firestore.v1beta1.StructuredQuery.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='google.firestore.v1beta1.StructuredQuery.Order.field', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='google.firestore.v1beta1.StructuredQuery.Order.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  ],
  serialized_start=1822,
  serialized_end=1974,
)

_STRUCTUREDQUERY_FIELDREFERENCE = _descriptor.Descriptor(
  name='FieldReference',
  full_name='google.firestore.v1beta1.StructuredQuery.FieldReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_path', full_name='google.firestore.v1beta1.StructuredQuery.FieldReference.field_path', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1976,
  serialized_end=2012,
)

_STRUCTUREDQUERY_PROJECTION = _descriptor.Descriptor(
  name='Projection',
  full_name='google.firestore.v1beta1.StructuredQuery.Projection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.firestore.v1beta1.StructuredQuery.Projection.fields', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=2014,
  serialized_end=2100,
)

_STRUCTUREDQUERY = _descriptor.Descriptor(
  name='StructuredQuery',
  full_name='google.firestore.v1beta1.StructuredQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='select', full_name='google.firestore.v1beta1.StructuredQuery.select', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='google.firestore.v1beta1.StructuredQuery.from', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='where', full_name='google.firestore.v1beta1.StructuredQuery.where', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.firestore.v1beta1.StructuredQuery.order_by', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_at', full_name='google.firestore.v1beta1.StructuredQuery.start_at', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_at', full_name='google.firestore.v1beta1.StructuredQuery.end_at', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='google.firestore.v1beta1.StructuredQuery.offset', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='google.firestore.v1beta1.StructuredQuery.limit', index=7,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STRUCTUREDQUERY_COLLECTIONSELECTOR, _STRUCTUREDQUERY_FILTER, _STRUCTUREDQUERY_COMPOSITEFILTER, _STRUCTUREDQUERY_FIELDFILTER, _STRUCTUREDQUERY_UNARYFILTER, _STRUCTUREDQUERY_ORDER, _STRUCTUREDQUERY_FIELDREFERENCE, _STRUCTUREDQUERY_PROJECTION, ],
  enum_types=[
    _STRUCTUREDQUERY_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=2171,
)


_CURSOR = _descriptor.Descriptor(
  name='Cursor',
  full_name='google.firestore.v1beta1.Cursor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='google.firestore.v1beta1.Cursor.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='before', full_name='google.firestore.v1beta1.Cursor.before', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=2173,
  serialized_end=2246,
)

_STRUCTUREDQUERY_COLLECTIONSELECTOR.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_FILTER.fields_by_name['composite_filter'].message_type = _STRUCTUREDQUERY_COMPOSITEFILTER
_STRUCTUREDQUERY_FILTER.fields_by_name['field_filter'].message_type = _STRUCTUREDQUERY_FIELDFILTER
_STRUCTUREDQUERY_FILTER.fields_by_name['unary_filter'].message_type = _STRUCTUREDQUERY_UNARYFILTER
_STRUCTUREDQUERY_FILTER.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type'].fields.append(
  _STRUCTUREDQUERY_FILTER.fields_by_name['composite_filter'])
_STRUCTUREDQUERY_FILTER.fields_by_name['composite_filter'].containing_oneof = _STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type']
_STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type'].fields.append(
  _STRUCTUREDQUERY_FILTER.fields_by_name['field_filter'])
_STRUCTUREDQUERY_FILTER.fields_by_name['field_filter'].containing_oneof = _STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type']
_STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type'].fields.append(
  _STRUCTUREDQUERY_FILTER.fields_by_name['unary_filter'])
_STRUCTUREDQUERY_FILTER.fields_by_name['unary_filter'].containing_oneof = _STRUCTUREDQUERY_FILTER.oneofs_by_name['filter_type']
_STRUCTUREDQUERY_COMPOSITEFILTER.fields_by_name['op'].enum_type = _STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR
_STRUCTUREDQUERY_COMPOSITEFILTER.fields_by_name['filters'].message_type = _STRUCTUREDQUERY_FILTER
_STRUCTUREDQUERY_COMPOSITEFILTER.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR.containing_type = _STRUCTUREDQUERY_COMPOSITEFILTER
_STRUCTUREDQUERY_FIELDFILTER.fields_by_name['field'].message_type = _STRUCTUREDQUERY_FIELDREFERENCE
_STRUCTUREDQUERY_FIELDFILTER.fields_by_name['op'].enum_type = _STRUCTUREDQUERY_FIELDFILTER_OPERATOR
_STRUCTUREDQUERY_FIELDFILTER.fields_by_name['value'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2._VALUE
_STRUCTUREDQUERY_FIELDFILTER.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_FIELDFILTER_OPERATOR.containing_type = _STRUCTUREDQUERY_FIELDFILTER
_STRUCTUREDQUERY_UNARYFILTER.fields_by_name['op'].enum_type = _STRUCTUREDQUERY_UNARYFILTER_OPERATOR
_STRUCTUREDQUERY_UNARYFILTER.fields_by_name['field'].message_type = _STRUCTUREDQUERY_FIELDREFERENCE
_STRUCTUREDQUERY_UNARYFILTER.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_UNARYFILTER_OPERATOR.containing_type = _STRUCTUREDQUERY_UNARYFILTER
_STRUCTUREDQUERY_UNARYFILTER.oneofs_by_name['operand_type'].fields.append(
  _STRUCTUREDQUERY_UNARYFILTER.fields_by_name['field'])
_STRUCTUREDQUERY_UNARYFILTER.fields_by_name['field'].containing_oneof = _STRUCTUREDQUERY_UNARYFILTER.oneofs_by_name['operand_type']
_STRUCTUREDQUERY_ORDER.fields_by_name['field'].message_type = _STRUCTUREDQUERY_FIELDREFERENCE
_STRUCTUREDQUERY_ORDER.fields_by_name['direction'].enum_type = _STRUCTUREDQUERY_DIRECTION
_STRUCTUREDQUERY_ORDER.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_FIELDREFERENCE.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY_PROJECTION.fields_by_name['fields'].message_type = _STRUCTUREDQUERY_FIELDREFERENCE
_STRUCTUREDQUERY_PROJECTION.containing_type = _STRUCTUREDQUERY
_STRUCTUREDQUERY.fields_by_name['select'].message_type = _STRUCTUREDQUERY_PROJECTION
_STRUCTUREDQUERY.fields_by_name['from'].message_type = _STRUCTUREDQUERY_COLLECTIONSELECTOR
_STRUCTUREDQUERY.fields_by_name['where'].message_type = _STRUCTUREDQUERY_FILTER
_STRUCTUREDQUERY.fields_by_name['order_by'].message_type = _STRUCTUREDQUERY_ORDER
_STRUCTUREDQUERY.fields_by_name['start_at'].message_type = _CURSOR
_STRUCTUREDQUERY.fields_by_name['end_at'].message_type = _CURSOR
_STRUCTUREDQUERY.fields_by_name['limit'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_STRUCTUREDQUERY_DIRECTION.containing_type = _STRUCTUREDQUERY
_CURSOR.fields_by_name['values'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2._VALUE
DESCRIPTOR.message_types_by_name['StructuredQuery'] = _STRUCTUREDQUERY
DESCRIPTOR.message_types_by_name['Cursor'] = _CURSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StructuredQuery = _reflection.GeneratedProtocolMessageType('StructuredQuery', (_message.Message,), dict(

  CollectionSelector = _reflection.GeneratedProtocolMessageType('CollectionSelector', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_COLLECTIONSELECTOR,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A selection of a collection, such as ``messages as m1``.
    
    
    Attributes:
        collection_id:
            The collection ID. When set, selects only collections with
            this ID.
        all_descendants:
            When false, selects only collections that are immediate
            children of the ``parent`` specified in the containing
            ``RunQueryRequest``. When true, selects all descendant
            collections.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.CollectionSelector)
    ))
  ,

  Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_FILTER,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A filter.
    
    
    Attributes:
        filter_type:
            The type of filter.
        composite_filter:
            A composite filter.
        field_filter:
            A filter on a document field.
        unary_filter:
            A filter that takes exactly one argument.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.Filter)
    ))
  ,

  CompositeFilter = _reflection.GeneratedProtocolMessageType('CompositeFilter', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_COMPOSITEFILTER,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A filter that merges multiple other filters using the given operator.
    
    
    Attributes:
        op:
            The operator for combining multiple filters.
        filters:
            The list of filters to combine. Must contain at least one
            filter.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.CompositeFilter)
    ))
  ,

  FieldFilter = _reflection.GeneratedProtocolMessageType('FieldFilter', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_FIELDFILTER,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A filter on a specific field.
    
    
    Attributes:
        field:
            The field to filter by.
        op:
            The operator to filter by.
        value:
            The value to compare to.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.FieldFilter)
    ))
  ,

  UnaryFilter = _reflection.GeneratedProtocolMessageType('UnaryFilter', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_UNARYFILTER,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A filter with a single operand.
    
    
    Attributes:
        op:
            The unary operator to apply.
        operand_type:
            The argument to the filter.
        field:
            The field to which to apply the operator.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.UnaryFilter)
    ))
  ,

  Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_ORDER,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """An order on a field.
    
    
    Attributes:
        field:
            The field to order by.
        direction:
            The direction to order by. Defaults to ``ASCENDING``.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.Order)
    ))
  ,

  FieldReference = _reflection.GeneratedProtocolMessageType('FieldReference', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_FIELDREFERENCE,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """A reference to a field, such as ``max(messages.time) as max_time``.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.FieldReference)
    ))
  ,

  Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), dict(
    DESCRIPTOR = _STRUCTUREDQUERY_PROJECTION,
    __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
    ,
    __doc__ = """The projection of document's fields to return.
    
    
    Attributes:
        fields:
            The fields to return.  If empty, all fields are returned. To
            only return the name of the document, use ``['__name__']``.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery.Projection)
    ))
  ,
  DESCRIPTOR = _STRUCTUREDQUERY,
  __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
  ,
  __doc__ = """A Firestore query.
  
  
  Attributes:
      select:
          The projection to return.
      from:
          The collections to query.
      where:
          The filter to apply.
      order_by:
          The order to apply to the query results.  Firestore guarantees
          a stable ordering through the following rules:  -  Any field
          required to appear in ``order_by``, that is not already
          specified in ``order_by``, is appended to the order in field
          name    order by default. -  If an order on ``__name__`` is
          not specified, it is appended by    default.  Fields are
          appended with the same sort direction as the last order
          specified, or 'ASCENDING' if no order was specified. For
          example:  -  ``SELECT * FROM Foo ORDER BY A`` becomes
          ``SELECT * FROM Foo ORDER BY A, __name__`` -  ``SELECT * FROM
          Foo ORDER BY A DESC`` becomes    ``SELECT * FROM Foo ORDER BY
          A DESC, __name__ DESC`` -  ``SELECT * FROM Foo WHERE A > 1``
          becomes    ``SELECT * FROM Foo WHERE A > 1 ORDER BY A,
          __name__``
      start_at:
          A starting point for the query results.
      end_at:
          A end point for the query results.
      offset:
          The number of results to skip.  Applies before limit, but
          after all other constraints. Must be >= 0 if specified.
      limit:
          The maximum number of results to return.  Applies after all
          other constraints. Must be >= 0 if specified.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.StructuredQuery)
  ))
_sym_db.RegisterMessage(StructuredQuery)
_sym_db.RegisterMessage(StructuredQuery.CollectionSelector)
_sym_db.RegisterMessage(StructuredQuery.Filter)
_sym_db.RegisterMessage(StructuredQuery.CompositeFilter)
_sym_db.RegisterMessage(StructuredQuery.FieldFilter)
_sym_db.RegisterMessage(StructuredQuery.UnaryFilter)
_sym_db.RegisterMessage(StructuredQuery.Order)
_sym_db.RegisterMessage(StructuredQuery.FieldReference)
_sym_db.RegisterMessage(StructuredQuery.Projection)

Cursor = _reflection.GeneratedProtocolMessageType('Cursor', (_message.Message,), dict(
  DESCRIPTOR = _CURSOR,
  __module__ = 'google.cloud.firestore_v1beta1.proto.query_pb2'
  ,
  __doc__ = """A position in a query result set.
  
  
  Attributes:
      values:
          The values that represent a position, in the order they appear
          in the order by clause of a query.  Can contain fewer values
          than specified in the order by clause.
      before:
          If the position is just before or just after the given values,
          relative to the sort order defined by the query.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.Cursor)
  ))
_sym_db.RegisterMessage(Cursor)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
