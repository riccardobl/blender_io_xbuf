# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pgex_ext/animations_kf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pgex.datas_pb2

from pgex.datas_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='pgex_ext/animations_kf.proto',
  package='pgex_ext',
  serialized_pb=_b('\n\x1cpgex_ext/animations_kf.proto\x12\x08pgex_ext\x1a\x10pgex/datas.proto\"X\n\x0b\x41nimationKF\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\x02\x12\x1d\n\x05\x63lips\x18\x04 \x03(\x0b\x32\x0e.pgex_ext.Clip\"e\n\x04\x43lip\x12+\n\ntransforms\x18\n \x01(\x0b\x32\x15.pgex_ext.TransformKFH\x00\x12#\n\x06\x63olors\x18\x0b \x01(\x0b\x32\x11.pgex_ext.ColorKFH\x00\x42\x0b\n\tkeyframes\"\x7f\n\x0bTransformKF\x12%\n\x0btranslation\x18\x01 \x01(\x0b\x32\x10.pgex_ext.Vec3KF\x12(\n\x08rotation\x18\x02 \x01(\x0b\x32\x16.pgex_ext.QuaternionKF\x12\x1f\n\x05scale\x18\x03 \x01(\x0b\x32\x10.pgex_ext.Vec3KF\"h\n\x06Vec3KF\x12\x1e\n\x01x\x18\x01 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01y\x18\x02 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01z\x18\x03 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\"\x8e\x01\n\x0cQuaternionKF\x12\x1e\n\x01x\x18\x01 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01y\x18\x02 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01z\x18\x03 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01w\x18\x04 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\"\x89\x01\n\x07\x43olorKF\x12\x1e\n\x01r\x18\x01 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01g\x18\x02 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01\x62\x18\x03 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\x12\x1e\n\x01\x61\x18\x04 \x01(\x0b\x32\x13.pgex_ext.KeyPoints\"\xe4\x01\n\tKeyPoints\x12\x1a\n\x0e\x64uration_ratio\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x11\n\x05value\x18\x02 \x03(\x02\x42\x02\x10\x01\x12?\n\rinterpolation\x18\x03 \x03(\x0e\x32$.pgex_ext.KeyPoints.InterpolationFctB\x02\x10\x01\x12-\n\rbezier_params\x18\x04 \x03(\x0b\x32\x16.pgex_ext.BezierParams\"8\n\x10InterpolationFct\x12\x0c\n\x08\x63onstant\x10\x01\x12\n\n\x06linear\x10\x02\x12\n\n\x06\x62\x65zier\x10\x03\"F\n\x0c\x42\x65zierParams\x12\x0c\n\x04h0_x\x18\x01 \x01(\x02\x12\x0c\n\x04h0_y\x18\x02 \x01(\x02\x12\x0c\n\x04h1_x\x18\x03 \x01(\x02\x12\x0c\n\x04h1_y\x18\x04 \x01(\x02:9\n\ranimations_kf\x12\n.pgex.Data\x18\xf5\x03 \x03(\x0b\x32\x15.pgex_ext.AnimationKFB\x02H\x03P\x00')
  ,
  dependencies=[pgex.datas_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


ANIMATIONS_KF_FIELD_NUMBER = 501
animations_kf = _descriptor.FieldDescriptor(
  name='animations_kf', full_name='pgex_ext.animations_kf', index=0,
  number=501, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_KEYPOINTS_INTERPOLATIONFCT = _descriptor.EnumDescriptor(
  name='InterpolationFct',
  full_name='pgex_ext.KeyPoints.InterpolationFct',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='constant', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='linear', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bezier', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=946,
  serialized_end=1002,
)
_sym_db.RegisterEnumDescriptor(_KEYPOINTS_INTERPOLATIONFCT)


_ANIMATIONKF = _descriptor.Descriptor(
  name='AnimationKF',
  full_name='pgex_ext.AnimationKF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pgex_ext.AnimationKF.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='pgex_ext.AnimationKF.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='pgex_ext.AnimationKF.duration', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clips', full_name='pgex_ext.AnimationKF.clips', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=60,
  serialized_end=148,
)


_CLIP = _descriptor.Descriptor(
  name='Clip',
  full_name='pgex_ext.Clip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transforms', full_name='pgex_ext.Clip.transforms', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='colors', full_name='pgex_ext.Clip.colors', index=1,
      number=11, type=11, cpp_type=10, label=1,
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
      name='keyframes', full_name='pgex_ext.Clip.keyframes',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=150,
  serialized_end=251,
)


_TRANSFORMKF = _descriptor.Descriptor(
  name='TransformKF',
  full_name='pgex_ext.TransformKF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='pgex_ext.TransformKF.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='pgex_ext.TransformKF.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='pgex_ext.TransformKF.scale', index=2,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=380,
)


_VEC3KF = _descriptor.Descriptor(
  name='Vec3KF',
  full_name='pgex_ext.Vec3KF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='pgex_ext.Vec3KF.x', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='pgex_ext.Vec3KF.y', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='pgex_ext.Vec3KF.z', index=2,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=486,
)


_QUATERNIONKF = _descriptor.Descriptor(
  name='QuaternionKF',
  full_name='pgex_ext.QuaternionKF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='pgex_ext.QuaternionKF.x', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='pgex_ext.QuaternionKF.y', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='pgex_ext.QuaternionKF.z', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='pgex_ext.QuaternionKF.w', index=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=489,
  serialized_end=631,
)


_COLORKF = _descriptor.Descriptor(
  name='ColorKF',
  full_name='pgex_ext.ColorKF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='pgex_ext.ColorKF.r', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='g', full_name='pgex_ext.ColorKF.g', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='pgex_ext.ColorKF.b', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='pgex_ext.ColorKF.a', index=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=771,
)


_KEYPOINTS = _descriptor.Descriptor(
  name='KeyPoints',
  full_name='pgex_ext.KeyPoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration_ratio', full_name='pgex_ext.KeyPoints.duration_ratio', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='value', full_name='pgex_ext.KeyPoints.value', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='interpolation', full_name='pgex_ext.KeyPoints.interpolation', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='bezier_params', full_name='pgex_ext.KeyPoints.bezier_params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYPOINTS_INTERPOLATIONFCT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=1002,
)


_BEZIERPARAMS = _descriptor.Descriptor(
  name='BezierParams',
  full_name='pgex_ext.BezierParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='h0_x', full_name='pgex_ext.BezierParams.h0_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h0_y', full_name='pgex_ext.BezierParams.h0_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h1_x', full_name='pgex_ext.BezierParams.h1_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h1_y', full_name='pgex_ext.BezierParams.h1_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1074,
)

_ANIMATIONKF.fields_by_name['clips'].message_type = _CLIP
_CLIP.fields_by_name['transforms'].message_type = _TRANSFORMKF
_CLIP.fields_by_name['colors'].message_type = _COLORKF
_CLIP.oneofs_by_name['keyframes'].fields.append(
  _CLIP.fields_by_name['transforms'])
_CLIP.fields_by_name['transforms'].containing_oneof = _CLIP.oneofs_by_name['keyframes']
_CLIP.oneofs_by_name['keyframes'].fields.append(
  _CLIP.fields_by_name['colors'])
_CLIP.fields_by_name['colors'].containing_oneof = _CLIP.oneofs_by_name['keyframes']
_TRANSFORMKF.fields_by_name['translation'].message_type = _VEC3KF
_TRANSFORMKF.fields_by_name['rotation'].message_type = _QUATERNIONKF
_TRANSFORMKF.fields_by_name['scale'].message_type = _VEC3KF
_VEC3KF.fields_by_name['x'].message_type = _KEYPOINTS
_VEC3KF.fields_by_name['y'].message_type = _KEYPOINTS
_VEC3KF.fields_by_name['z'].message_type = _KEYPOINTS
_QUATERNIONKF.fields_by_name['x'].message_type = _KEYPOINTS
_QUATERNIONKF.fields_by_name['y'].message_type = _KEYPOINTS
_QUATERNIONKF.fields_by_name['z'].message_type = _KEYPOINTS
_QUATERNIONKF.fields_by_name['w'].message_type = _KEYPOINTS
_COLORKF.fields_by_name['r'].message_type = _KEYPOINTS
_COLORKF.fields_by_name['g'].message_type = _KEYPOINTS
_COLORKF.fields_by_name['b'].message_type = _KEYPOINTS
_COLORKF.fields_by_name['a'].message_type = _KEYPOINTS
_KEYPOINTS.fields_by_name['interpolation'].enum_type = _KEYPOINTS_INTERPOLATIONFCT
_KEYPOINTS.fields_by_name['bezier_params'].message_type = _BEZIERPARAMS
_KEYPOINTS_INTERPOLATIONFCT.containing_type = _KEYPOINTS
DESCRIPTOR.message_types_by_name['AnimationKF'] = _ANIMATIONKF
DESCRIPTOR.message_types_by_name['Clip'] = _CLIP
DESCRIPTOR.message_types_by_name['TransformKF'] = _TRANSFORMKF
DESCRIPTOR.message_types_by_name['Vec3KF'] = _VEC3KF
DESCRIPTOR.message_types_by_name['QuaternionKF'] = _QUATERNIONKF
DESCRIPTOR.message_types_by_name['ColorKF'] = _COLORKF
DESCRIPTOR.message_types_by_name['KeyPoints'] = _KEYPOINTS
DESCRIPTOR.message_types_by_name['BezierParams'] = _BEZIERPARAMS
DESCRIPTOR.extensions_by_name['animations_kf'] = animations_kf

AnimationKF = _reflection.GeneratedProtocolMessageType('AnimationKF', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONKF,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.AnimationKF)
  ))
_sym_db.RegisterMessage(AnimationKF)

Clip = _reflection.GeneratedProtocolMessageType('Clip', (_message.Message,), dict(
  DESCRIPTOR = _CLIP,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.Clip)
  ))
_sym_db.RegisterMessage(Clip)

TransformKF = _reflection.GeneratedProtocolMessageType('TransformKF', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMKF,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.TransformKF)
  ))
_sym_db.RegisterMessage(TransformKF)

Vec3KF = _reflection.GeneratedProtocolMessageType('Vec3KF', (_message.Message,), dict(
  DESCRIPTOR = _VEC3KF,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.Vec3KF)
  ))
_sym_db.RegisterMessage(Vec3KF)

QuaternionKF = _reflection.GeneratedProtocolMessageType('QuaternionKF', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNIONKF,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.QuaternionKF)
  ))
_sym_db.RegisterMessage(QuaternionKF)

ColorKF = _reflection.GeneratedProtocolMessageType('ColorKF', (_message.Message,), dict(
  DESCRIPTOR = _COLORKF,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.ColorKF)
  ))
_sym_db.RegisterMessage(ColorKF)

KeyPoints = _reflection.GeneratedProtocolMessageType('KeyPoints', (_message.Message,), dict(
  DESCRIPTOR = _KEYPOINTS,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.KeyPoints)
  ))
_sym_db.RegisterMessage(KeyPoints)

BezierParams = _reflection.GeneratedProtocolMessageType('BezierParams', (_message.Message,), dict(
  DESCRIPTOR = _BEZIERPARAMS,
  __module__ = 'pgex_ext.animations_kf_pb2'
  # @@protoc_insertion_point(class_scope:pgex_ext.BezierParams)
  ))
_sym_db.RegisterMessage(BezierParams)

animations_kf.message_type = _ANIMATIONKF
pgex.datas_pb2.Data.RegisterExtension(animations_kf)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_KEYPOINTS.fields_by_name['duration_ratio'].has_options = True
_KEYPOINTS.fields_by_name['duration_ratio']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_KEYPOINTS.fields_by_name['value'].has_options = True
_KEYPOINTS.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_KEYPOINTS.fields_by_name['interpolation'].has_options = True
_KEYPOINTS.fields_by_name['interpolation']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)