# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='repo-command-response.proto',
  package='ndn_message',
  serialized_pb='\n\x1brepo-command-response.proto\x12\x0bndn_message\"\x96\x02\n\x1aRepoCommandResponseMessage\x12[\n\x15repo_command_response\x18\xcf\x01 \x02(\x0b\x32;.ndn_message.RepoCommandResponseMessage.RepoCommandResponse\x1a\x9a\x01\n\x13RepoCommandResponse\x12\x13\n\nprocess_id\x18\xce\x01 \x01(\x04\x12\x14\n\x0bstatus_code\x18\xd0\x01 \x02(\x04\x12\x17\n\x0estart_block_id\x18\xcc\x01 \x01(\x04\x12\x15\n\x0c\x65nd_block_id\x18\xcd\x01 \x01(\x04\x12\x13\n\ninsert_num\x18\xd1\x01 \x01(\x04\x12\x13\n\ndelete_num\x18\xd2\x01 \x01(\x04')




_REPOCOMMANDRESPONSEMESSAGE_REPOCOMMANDRESPONSE = descriptor.Descriptor(
  name='RepoCommandResponse',
  full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='process_id', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.process_id', index=0,
      number=206, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status_code', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.status_code', index=1,
      number=208, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_block_id', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.start_block_id', index=2,
      number=204, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_block_id', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.end_block_id', index=3,
      number=205, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='insert_num', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.insert_num', index=4,
      number=209, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delete_num', full_name='ndn_message.RepoCommandResponseMessage.RepoCommandResponse.delete_num', index=5,
      number=210, type=4, cpp_type=4, label=1,
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
  serialized_start=169,
  serialized_end=323,
)

_REPOCOMMANDRESPONSEMESSAGE = descriptor.Descriptor(
  name='RepoCommandResponseMessage',
  full_name='ndn_message.RepoCommandResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='repo_command_response', full_name='ndn_message.RepoCommandResponseMessage.repo_command_response', index=0,
      number=207, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REPOCOMMANDRESPONSEMESSAGE_REPOCOMMANDRESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=323,
)

_REPOCOMMANDRESPONSEMESSAGE_REPOCOMMANDRESPONSE.containing_type = _REPOCOMMANDRESPONSEMESSAGE;
_REPOCOMMANDRESPONSEMESSAGE.fields_by_name['repo_command_response'].message_type = _REPOCOMMANDRESPONSEMESSAGE_REPOCOMMANDRESPONSE
DESCRIPTOR.message_types_by_name['RepoCommandResponseMessage'] = _REPOCOMMANDRESPONSEMESSAGE

class RepoCommandResponseMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class RepoCommandResponse(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _REPOCOMMANDRESPONSEMESSAGE_REPOCOMMANDRESPONSE
    
    # @@protoc_insertion_point(class_scope:ndn_message.RepoCommandResponseMessage.RepoCommandResponse)
  DESCRIPTOR = _REPOCOMMANDRESPONSEMESSAGE
  
  # @@protoc_insertion_point(class_scope:ndn_message.RepoCommandResponseMessage)

# @@protoc_insertion_point(module_scope)
