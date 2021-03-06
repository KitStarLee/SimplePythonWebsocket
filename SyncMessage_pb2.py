# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SyncMessage.proto

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
  name='SyncMessage.proto',
  package='PBMessage',
  syntax='proto2',
  serialized_pb=_b('\n\x11SyncMessage.proto\x12\tPBMessage\"\xc9\x01\n\x08UserInfo\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\r\n\x05level\x18\x02 \x02(\x05\x12\x14\n\x0chighestScore\x18\x04 \x02(\x02\x12\x0f\n\x07ranking\x18\x05 \x02(\x05\x12*\n\x06status\x18\x06 \x02(\x0e\x32\x1a.PBMessage.UserInfo.Status\x12\x12\n\nkillNumber\x18\x07 \x02(\x05\x12\x13\n\x0b\x64\x65\x61thNumber\x18\x08 \x02(\x05\"!\n\x06Status\x12\n\n\x06ONLIEN\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\"R\n\x0cMessageLogin\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x0e\n\x06status\x18\x03 \x02(\t\x12\x0f\n\x07\x63hannel\x18\x04 \x02(\t\" \n\rMessageLogout\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\"\xeb\x01\n\nWeaponInfo\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\x34\n\nweaponType\x18\x02 \x02(\x0e\x32 .PBMessage.WeaponInfo.WeaponType\x12\x0e\n\x06target\x18\x03 \x02(\t\"\x85\x01\n\nWeaponType\x12\x0e\n\nMachineGun\x10\x00\x12\r\n\tPlasmaGun\x10\x01\x12\x0c\n\x08JetFlame\x10\x02\x12\x0f\n\x0bLightShield\x10\x03\x12\x11\n\rFireWhirlwind\x10\x04\x12\x0b\n\x07Missile\x10\x05\x12\x0f\n\x0bOrdinaryGun\x10\x06\x12\x08\n\x04None\x10\x07\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"5\n\x07Vector4\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\x12\t\n\x01w\x18\x04 \x02(\x02\"\x1f\n\x07Vector2\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\"\x8e\x01\n\rTransformData\x12\x0f\n\x07\x61\x63\x63ount\x18\x04 \x02(\t\x12\n\n\x02\x63\x66\x18\x05 \x02(\x02\x12\x1d\n\x01p\x18\x01 \x02(\x0b\x32\x12.PBMessage.Vector3\x12\x1d\n\x01r\x18\x02 \x02(\x0b\x32\x12.PBMessage.Vector3\x12\"\n\x06rotate\x18\x03 \x02(\x0b\x32\x12.PBMessage.Vector4\"v\n\x12\x44irectionSpeedData\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\r\n\x05\x61ngle\x18\x02 \x02(\x02\x12\x15\n\rmRockerIsMove\x18\x03 \x02(\x08\x12)\n\rcircularAngle\x18\x04 \x02(\x0b\x32\x12.PBMessage.Vector2\"C\n\x0fWeaponGunRotate\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x02(\t\x12\x10\n\x08isAttack\x18\x02 \x02(\x08\x12\r\n\x05\x61ngle\x18\x01 \x02(\x02\"0\n\x1dMessageGenerateExistedClients\x12\x0f\n\x07\x63lients\x18\x02 \x03(\t\"\xa6\x02\n\nObjectInfo\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\r\n\x05MaxHp\x18\x02 \x02(\x02\x12\n\n\x02Hp\x18\x03 \x02(\x02\x12\x10\n\x08\x41tkValue\x18\x04 \x02(\x02\x12\x10\n\x08\x44\x65\x66Value\x18\x05 \x02(\x02\x12\r\n\x05Level\x18\x06 \x02(\x02\x12\r\n\x05Score\x18\x07 \x02(\x02\x12\x12\n\nKillNumber\x18\x08 \x02(\x05\x12\x13\n\x0b\x44\x65\x61thNumber\x18\t \x02(\x05\x12\x34\n\nobjectType\x18\n \x02(\x0e\x32 .PBMessage.ObjectInfo.ObjectType\"K\n\nObjectType\x12\x07\n\x03Min\x10\x00\x12\t\n\x05\x42itch\x10\x01\x12\t\n\x05\x41ngel\x10\x02\x12\n\n\x06Toilet\x10\x03\x12\t\n\x05Villa\x10\x04\x12\x07\n\x03Max\x10\x05\"0\n\x0eMessageOnDeath\x12\x10\n\x08\x41ttacker\x18\x01 \x02(\t\x12\x0c\n\x04\x44\x65\x61\x64\x18\x02 \x02(\t\"4\n\x11OrdinaryGunAttack\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x02(\t\x12\x0e\n\x06\x41ttack\x18\x02 \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USERINFO_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='PBMessage.UserInfo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONLIEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=201,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_USERINFO_STATUS)

_WEAPONINFO_WEAPONTYPE = _descriptor.EnumDescriptor(
  name='WeaponType',
  full_name='PBMessage.WeaponInfo.WeaponType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MachineGun', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PlasmaGun', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JetFlame', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LightShield', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FireWhirlwind', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Missile', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrdinaryGun', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='None', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=457,
  serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_WEAPONINFO_WEAPONTYPE)

_OBJECTINFO_OBJECTTYPE = _descriptor.EnumDescriptor(
  name='ObjectType',
  full_name='PBMessage.ObjectInfo.ObjectType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Min', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bitch', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Angel', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Toilet', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Villa', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1328,
  serialized_end=1403,
)
_sym_db.RegisterEnumDescriptor(_OBJECTINFO_OBJECTTYPE)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='PBMessage.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.UserInfo.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='PBMessage.UserInfo.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highestScore', full_name='PBMessage.UserInfo.highestScore', index=2,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranking', full_name='PBMessage.UserInfo.ranking', index=3,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='PBMessage.UserInfo.status', index=4,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='killNumber', full_name='PBMessage.UserInfo.killNumber', index=5,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deathNumber', full_name='PBMessage.UserInfo.deathNumber', index=6,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERINFO_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=234,
)


_MESSAGELOGIN = _descriptor.Descriptor(
  name='MessageLogin',
  full_name='PBMessage.MessageLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.MessageLogin.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='PBMessage.MessageLogin.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='PBMessage.MessageLogin.status', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='PBMessage.MessageLogin.channel', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  serialized_start=236,
  serialized_end=318,
)


_MESSAGELOGOUT = _descriptor.Descriptor(
  name='MessageLogout',
  full_name='PBMessage.MessageLogout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.MessageLogout.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=320,
  serialized_end=352,
)


_WEAPONINFO = _descriptor.Descriptor(
  name='WeaponInfo',
  full_name='PBMessage.WeaponInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.WeaponInfo.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weaponType', full_name='PBMessage.WeaponInfo.weaponType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='PBMessage.WeaponInfo.target', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEAPONINFO_WEAPONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=590,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='PBMessage.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PBMessage.Vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PBMessage.Vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='PBMessage.Vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=592,
  serialized_end=634,
)


_VECTOR4 = _descriptor.Descriptor(
  name='Vector4',
  full_name='PBMessage.Vector4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PBMessage.Vector4.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PBMessage.Vector4.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='PBMessage.Vector4.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='PBMessage.Vector4.w', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=636,
  serialized_end=689,
)


_VECTOR2 = _descriptor.Descriptor(
  name='Vector2',
  full_name='PBMessage.Vector2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='PBMessage.Vector2.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='PBMessage.Vector2.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=691,
  serialized_end=722,
)


_TRANSFORMDATA = _descriptor.Descriptor(
  name='TransformData',
  full_name='PBMessage.TransformData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.TransformData.account', index=0,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cf', full_name='PBMessage.TransformData.cf', index=1,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p', full_name='PBMessage.TransformData.p', index=2,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r', full_name='PBMessage.TransformData.r', index=3,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotate', full_name='PBMessage.TransformData.rotate', index=4,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=725,
  serialized_end=867,
)


_DIRECTIONSPEEDDATA = _descriptor.Descriptor(
  name='DirectionSpeedData',
  full_name='PBMessage.DirectionSpeedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.DirectionSpeedData.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle', full_name='PBMessage.DirectionSpeedData.angle', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mRockerIsMove', full_name='PBMessage.DirectionSpeedData.mRockerIsMove', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='circularAngle', full_name='PBMessage.DirectionSpeedData.circularAngle', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=869,
  serialized_end=987,
)


_WEAPONGUNROTATE = _descriptor.Descriptor(
  name='WeaponGunRotate',
  full_name='PBMessage.WeaponGunRotate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.WeaponGunRotate.account', index=0,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isAttack', full_name='PBMessage.WeaponGunRotate.isAttack', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle', full_name='PBMessage.WeaponGunRotate.angle', index=2,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=989,
  serialized_end=1056,
)


_MESSAGEGENERATEEXISTEDCLIENTS = _descriptor.Descriptor(
  name='MessageGenerateExistedClients',
  full_name='PBMessage.MessageGenerateExistedClients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients', full_name='PBMessage.MessageGenerateExistedClients.clients', index=0,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1058,
  serialized_end=1106,
)


_OBJECTINFO = _descriptor.Descriptor(
  name='ObjectInfo',
  full_name='PBMessage.ObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.ObjectInfo.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxHp', full_name='PBMessage.ObjectInfo.MaxHp', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hp', full_name='PBMessage.ObjectInfo.Hp', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtkValue', full_name='PBMessage.ObjectInfo.AtkValue', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DefValue', full_name='PBMessage.ObjectInfo.DefValue', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PBMessage.ObjectInfo.Level', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Score', full_name='PBMessage.ObjectInfo.Score', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='KillNumber', full_name='PBMessage.ObjectInfo.KillNumber', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeathNumber', full_name='PBMessage.ObjectInfo.DeathNumber', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objectType', full_name='PBMessage.ObjectInfo.objectType', index=9,
      number=10, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBJECTINFO_OBJECTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1109,
  serialized_end=1403,
)


_MESSAGEONDEATH = _descriptor.Descriptor(
  name='MessageOnDeath',
  full_name='PBMessage.MessageOnDeath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Attacker', full_name='PBMessage.MessageOnDeath.Attacker', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Dead', full_name='PBMessage.MessageOnDeath.Dead', index=1,
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
  serialized_start=1405,
  serialized_end=1453,
)


_ORDINARYGUNATTACK = _descriptor.Descriptor(
  name='OrdinaryGunAttack',
  full_name='PBMessage.OrdinaryGunAttack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='PBMessage.OrdinaryGunAttack.account', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Attack', full_name='PBMessage.OrdinaryGunAttack.Attack', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=1455,
  serialized_end=1507,
)

_USERINFO.fields_by_name['status'].enum_type = _USERINFO_STATUS
_USERINFO_STATUS.containing_type = _USERINFO
_WEAPONINFO.fields_by_name['weaponType'].enum_type = _WEAPONINFO_WEAPONTYPE
_WEAPONINFO_WEAPONTYPE.containing_type = _WEAPONINFO
_TRANSFORMDATA.fields_by_name['p'].message_type = _VECTOR3
_TRANSFORMDATA.fields_by_name['r'].message_type = _VECTOR3
_TRANSFORMDATA.fields_by_name['rotate'].message_type = _VECTOR4
_DIRECTIONSPEEDDATA.fields_by_name['circularAngle'].message_type = _VECTOR2
_OBJECTINFO.fields_by_name['objectType'].enum_type = _OBJECTINFO_OBJECTTYPE
_OBJECTINFO_OBJECTTYPE.containing_type = _OBJECTINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['MessageLogin'] = _MESSAGELOGIN
DESCRIPTOR.message_types_by_name['MessageLogout'] = _MESSAGELOGOUT
DESCRIPTOR.message_types_by_name['WeaponInfo'] = _WEAPONINFO
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Vector4'] = _VECTOR4
DESCRIPTOR.message_types_by_name['Vector2'] = _VECTOR2
DESCRIPTOR.message_types_by_name['TransformData'] = _TRANSFORMDATA
DESCRIPTOR.message_types_by_name['DirectionSpeedData'] = _DIRECTIONSPEEDDATA
DESCRIPTOR.message_types_by_name['WeaponGunRotate'] = _WEAPONGUNROTATE
DESCRIPTOR.message_types_by_name['MessageGenerateExistedClients'] = _MESSAGEGENERATEEXISTEDCLIENTS
DESCRIPTOR.message_types_by_name['ObjectInfo'] = _OBJECTINFO
DESCRIPTOR.message_types_by_name['MessageOnDeath'] = _MESSAGEONDEATH
DESCRIPTOR.message_types_by_name['OrdinaryGunAttack'] = _ORDINARYGUNATTACK

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

MessageLogin = _reflection.GeneratedProtocolMessageType('MessageLogin', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGELOGIN,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.MessageLogin)
  ))
_sym_db.RegisterMessage(MessageLogin)

MessageLogout = _reflection.GeneratedProtocolMessageType('MessageLogout', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGELOGOUT,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.MessageLogout)
  ))
_sym_db.RegisterMessage(MessageLogout)

WeaponInfo = _reflection.GeneratedProtocolMessageType('WeaponInfo', (_message.Message,), dict(
  DESCRIPTOR = _WEAPONINFO,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.WeaponInfo)
  ))
_sym_db.RegisterMessage(WeaponInfo)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Vector4 = _reflection.GeneratedProtocolMessageType('Vector4', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR4,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.Vector4)
  ))
_sym_db.RegisterMessage(Vector4)

Vector2 = _reflection.GeneratedProtocolMessageType('Vector2', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR2,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.Vector2)
  ))
_sym_db.RegisterMessage(Vector2)

TransformData = _reflection.GeneratedProtocolMessageType('TransformData', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMDATA,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.TransformData)
  ))
_sym_db.RegisterMessage(TransformData)

DirectionSpeedData = _reflection.GeneratedProtocolMessageType('DirectionSpeedData', (_message.Message,), dict(
  DESCRIPTOR = _DIRECTIONSPEEDDATA,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.DirectionSpeedData)
  ))
_sym_db.RegisterMessage(DirectionSpeedData)

WeaponGunRotate = _reflection.GeneratedProtocolMessageType('WeaponGunRotate', (_message.Message,), dict(
  DESCRIPTOR = _WEAPONGUNROTATE,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.WeaponGunRotate)
  ))
_sym_db.RegisterMessage(WeaponGunRotate)

MessageGenerateExistedClients = _reflection.GeneratedProtocolMessageType('MessageGenerateExistedClients', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEGENERATEEXISTEDCLIENTS,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.MessageGenerateExistedClients)
  ))
_sym_db.RegisterMessage(MessageGenerateExistedClients)

ObjectInfo = _reflection.GeneratedProtocolMessageType('ObjectInfo', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTINFO,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.ObjectInfo)
  ))
_sym_db.RegisterMessage(ObjectInfo)

MessageOnDeath = _reflection.GeneratedProtocolMessageType('MessageOnDeath', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEONDEATH,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.MessageOnDeath)
  ))
_sym_db.RegisterMessage(MessageOnDeath)

OrdinaryGunAttack = _reflection.GeneratedProtocolMessageType('OrdinaryGunAttack', (_message.Message,), dict(
  DESCRIPTOR = _ORDINARYGUNATTACK,
  __module__ = 'SyncMessage_pb2'
  # @@protoc_insertion_point(class_scope:PBMessage.OrdinaryGunAttack)
  ))
_sym_db.RegisterMessage(OrdinaryGunAttack)


# @@protoc_insertion_point(module_scope)
