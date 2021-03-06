# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbuf/meshes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xbuf/meshes.proto',
  package='xbuf',
  serialized_pb=_b('\n\x11xbuf/meshes.proto\x12\x04xbuf\"\x9a\x02\n\x04Mesh\x12\n\n\x02id\x18\x01 \x02(\t\x12\'\n\tprimitive\x18\x02 \x02(\x0e\x32\x14.xbuf.Mesh.Primitive\x12\x0e\n\x03lod\x18\x03 \x01(\r:\x01\x30\x12\'\n\x0cvertexArrays\x18\x04 \x03(\x0b\x32\x11.xbuf.VertexArray\x12%\n\x0bindexArrays\x18\x05 \x03(\x0b\x32\x10.xbuf.IndexArray\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x18\n\x04skin\x18\x07 \x01(\x0b\x32\n.xbuf.Skin\"U\n\tPrimitive\x12\n\n\x06points\x10\x01\x12\t\n\x05lines\x10\x02\x12\x0e\n\nline_strip\x10\x03\x12\r\n\ttriangles\x10\x04\x12\x12\n\x0etriangle_strip\x10\x05\"\xab\x03\n\x0bVertexArray\x12(\n\x06\x61ttrib\x18\x01 \x02(\x0e\x32\x18.xbuf.VertexArray.Attrib\x12\x10\n\x05morph\x18\x02 \x01(\r:\x01\x30\x12#\n\x06\x66loats\x18\x03 \x01(\x0b\x32\x11.xbuf.FloatBufferH\x00\"\xb0\x02\n\x06\x41ttrib\x12\x0c\n\x08position\x10\x01\x12\n\n\x06normal\x10\x02\x12\x0b\n\x07tangent\x10\x03\x12\x0c\n\x08tangent2\x10\x0f\x12\x0c\n\x08tangent3\x10\x10\x12\x0c\n\x08tangent4\x10\x11\x12\x0c\n\x08tangent5\x10\x12\x12\x0c\n\x08tangent6\x10\x13\x12\x0c\n\x08tangent7\x10\x14\x12\x0c\n\x08tangent8\x10\x15\x12\x0c\n\x08tangent9\x10\x16\x12\t\n\x05\x63olor\x10\x05\x12\x0c\n\x08texcoord\x10\x06\x12\r\n\ttexcoord2\x10\x07\x12\r\n\ttexcoord3\x10\x08\x12\r\n\ttexcoord4\x10\t\x12\r\n\ttexcoord5\x10\n\x12\r\n\ttexcoord6\x10\x0b\x12\r\n\ttexcoord7\x10\x0c\x12\r\n\ttexcoord8\x10\r\x12\r\n\ttexcoord9\x10\x0e\x42\x08\n\x06\x62uffer\"8\n\nIndexArray\x12 \n\x04ints\x18\x01 \x01(\x0b\x32\x10.xbuf.UintBufferH\x00\x42\x08\n\x06\x62uffer\"2\n\x0b\x46loatBuffer\x12\x12\n\x06values\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x0f\n\x04step\x18\x02 \x02(\r:\x01\x31\"1\n\nUintBuffer\x12\x12\n\x06values\x18\x01 \x03(\rB\x02\x10\x01\x12\x0f\n\x04step\x18\x02 \x02(\r:\x01\x31\"_\n\x04Skin\x12\x15\n\tboneCount\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x15\n\tboneIndex\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x16\n\nboneWeight\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\x11\n\tboneNames\x18\x05 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESH_PRIMITIVE = _descriptor.EnumDescriptor(
  name='Primitive',
  full_name='xbuf.Mesh.Primitive',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='points', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='lines', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='line_strip', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='triangles', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='triangle_strip', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=225,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_MESH_PRIMITIVE)

_VERTEXARRAY_ATTRIB = _descriptor.EnumDescriptor(
  name='Attrib',
  full_name='xbuf.VertexArray.Attrib',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='position', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='normal', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent2', index=3, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent3', index=4, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent4', index=5, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent5', index=6, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent6', index=7, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent7', index=8, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent8', index=9, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tangent9', index=10, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='color', index=11, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord', index=12, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord2', index=13, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord3', index=14, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord4', index=15, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord5', index=16, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord6', index=17, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord7', index=18, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord8', index=19, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='texcoord9', index=20, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=426,
  serialized_end=730,
)
_sym_db.RegisterEnumDescriptor(_VERTEXARRAY_ATTRIB)


_MESH = _descriptor.Descriptor(
  name='Mesh',
  full_name='xbuf.Mesh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xbuf.Mesh.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primitive', full_name='xbuf.Mesh.primitive', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lod', full_name='xbuf.Mesh.lod', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertexArrays', full_name='xbuf.Mesh.vertexArrays', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexArrays', full_name='xbuf.Mesh.indexArrays', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='xbuf.Mesh.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skin', full_name='xbuf.Mesh.skin', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESH_PRIMITIVE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=310,
)


_VERTEXARRAY = _descriptor.Descriptor(
  name='VertexArray',
  full_name='xbuf.VertexArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attrib', full_name='xbuf.VertexArray.attrib', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='morph', full_name='xbuf.VertexArray.morph', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='floats', full_name='xbuf.VertexArray.floats', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VERTEXARRAY_ATTRIB,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='buffer', full_name='xbuf.VertexArray.buffer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=313,
  serialized_end=740,
)


_INDEXARRAY = _descriptor.Descriptor(
  name='IndexArray',
  full_name='xbuf.IndexArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ints', full_name='xbuf.IndexArray.ints', index=0,
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
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='buffer', full_name='xbuf.IndexArray.buffer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=742,
  serialized_end=798,
)


_FLOATBUFFER = _descriptor.Descriptor(
  name='FloatBuffer',
  full_name='xbuf.FloatBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='xbuf.FloatBuffer.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='step', full_name='xbuf.FloatBuffer.step', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=850,
)


_UINTBUFFER = _descriptor.Descriptor(
  name='UintBuffer',
  full_name='xbuf.UintBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='xbuf.UintBuffer.values', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='step', full_name='xbuf.UintBuffer.step', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=852,
  serialized_end=901,
)


_SKIN = _descriptor.Descriptor(
  name='Skin',
  full_name='xbuf.Skin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boneCount', full_name='xbuf.Skin.boneCount', index=0,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='boneIndex', full_name='xbuf.Skin.boneIndex', index=1,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='boneWeight', full_name='xbuf.Skin.boneWeight', index=2,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='boneNames', full_name='xbuf.Skin.boneNames', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=903,
  serialized_end=998,
)

_MESH.fields_by_name['primitive'].enum_type = _MESH_PRIMITIVE
_MESH.fields_by_name['vertexArrays'].message_type = _VERTEXARRAY
_MESH.fields_by_name['indexArrays'].message_type = _INDEXARRAY
_MESH.fields_by_name['skin'].message_type = _SKIN
_MESH_PRIMITIVE.containing_type = _MESH
_VERTEXARRAY.fields_by_name['attrib'].enum_type = _VERTEXARRAY_ATTRIB
_VERTEXARRAY.fields_by_name['floats'].message_type = _FLOATBUFFER
_VERTEXARRAY_ATTRIB.containing_type = _VERTEXARRAY
_VERTEXARRAY.oneofs_by_name['buffer'].fields.append(
  _VERTEXARRAY.fields_by_name['floats'])
_VERTEXARRAY.fields_by_name['floats'].containing_oneof = _VERTEXARRAY.oneofs_by_name['buffer']
_INDEXARRAY.fields_by_name['ints'].message_type = _UINTBUFFER
_INDEXARRAY.oneofs_by_name['buffer'].fields.append(
  _INDEXARRAY.fields_by_name['ints'])
_INDEXARRAY.fields_by_name['ints'].containing_oneof = _INDEXARRAY.oneofs_by_name['buffer']
DESCRIPTOR.message_types_by_name['Mesh'] = _MESH
DESCRIPTOR.message_types_by_name['VertexArray'] = _VERTEXARRAY
DESCRIPTOR.message_types_by_name['IndexArray'] = _INDEXARRAY
DESCRIPTOR.message_types_by_name['FloatBuffer'] = _FLOATBUFFER
DESCRIPTOR.message_types_by_name['UintBuffer'] = _UINTBUFFER
DESCRIPTOR.message_types_by_name['Skin'] = _SKIN

Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), dict(
  DESCRIPTOR = _MESH,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Mesh)
  ))
_sym_db.RegisterMessage(Mesh)

VertexArray = _reflection.GeneratedProtocolMessageType('VertexArray', (_message.Message,), dict(
  DESCRIPTOR = _VERTEXARRAY,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.VertexArray)
  ))
_sym_db.RegisterMessage(VertexArray)

IndexArray = _reflection.GeneratedProtocolMessageType('IndexArray', (_message.Message,), dict(
  DESCRIPTOR = _INDEXARRAY,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.IndexArray)
  ))
_sym_db.RegisterMessage(IndexArray)

FloatBuffer = _reflection.GeneratedProtocolMessageType('FloatBuffer', (_message.Message,), dict(
  DESCRIPTOR = _FLOATBUFFER,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.FloatBuffer)
  ))
_sym_db.RegisterMessage(FloatBuffer)

UintBuffer = _reflection.GeneratedProtocolMessageType('UintBuffer', (_message.Message,), dict(
  DESCRIPTOR = _UINTBUFFER,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.UintBuffer)
  ))
_sym_db.RegisterMessage(UintBuffer)

Skin = _reflection.GeneratedProtocolMessageType('Skin', (_message.Message,), dict(
  DESCRIPTOR = _SKIN,
  __module__ = 'xbuf.meshes_pb2'
  # @@protoc_insertion_point(class_scope:xbuf.Skin)
  ))
_sym_db.RegisterMessage(Skin)


_FLOATBUFFER.fields_by_name['values'].has_options = True
_FLOATBUFFER.fields_by_name['values']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_UINTBUFFER.fields_by_name['values'].has_options = True
_UINTBUFFER.fields_by_name['values']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SKIN.fields_by_name['boneCount'].has_options = True
_SKIN.fields_by_name['boneCount']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SKIN.fields_by_name['boneIndex'].has_options = True
_SKIN.fields_by_name['boneIndex']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SKIN.fields_by_name['boneWeight'].has_options = True
_SKIN.fields_by_name['boneWeight']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
