# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transaction.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'transaction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11transaction.proto\x12\x0btransaction\"c\n\x12TransactionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\"6\n\x13TransactionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"K\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\x12\x0c\n\x04type\x18\x04 \x01(\t\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"W\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\"A\n\x0fTransactionList\x12.\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x18.transaction.Transaction2\xda\x02\n\x12TransactionService\x12S\n\x0e\x41\x64\x64Transaction\x12\x1f.transaction.TransactionRequest\x1a .transaction.TransactionResponse\x12I\n\x0fGetTransactions\x12\x18.transaction.UserRequest\x1a\x1c.transaction.TransactionList\x12Q\n\x11UpdateTransaction\x12\x1a.transaction.UpdateRequest\x1a .transaction.TransactionResponse\x12Q\n\x11\x44\x65leteTransaction\x12\x1a.transaction.DeleteRequest\x1a .transaction.TransactionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSACTIONREQUEST']._serialized_start=34
  _globals['_TRANSACTIONREQUEST']._serialized_end=133
  _globals['_TRANSACTIONRESPONSE']._serialized_start=135
  _globals['_TRANSACTIONRESPONSE']._serialized_end=189
  _globals['_UPDATEREQUEST']._serialized_start=191
  _globals['_UPDATEREQUEST']._serialized_end=266
  _globals['_DELETEREQUEST']._serialized_start=268
  _globals['_DELETEREQUEST']._serialized_end=295
  _globals['_USERREQUEST']._serialized_start=297
  _globals['_USERREQUEST']._serialized_end=327
  _globals['_TRANSACTION']._serialized_start=329
  _globals['_TRANSACTION']._serialized_end=416
  _globals['_TRANSACTIONLIST']._serialized_start=418
  _globals['_TRANSACTIONLIST']._serialized_end=483
  _globals['_TRANSACTIONSERVICE']._serialized_start=486
  _globals['_TRANSACTIONSERVICE']._serialized_end=832
# @@protoc_insertion_point(module_scope)
