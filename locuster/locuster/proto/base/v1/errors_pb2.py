# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v1/errors.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x62\x61se/v1/errors.proto\x12\x07\x62\x61se.v1\"Q\n\rErrorResponse\x12&\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x12.base.v1.ErrorCodeR\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message*\xc1\x15\n\tErrorCode\x12\x1a\n\x16\x45RROR_CODE_UNSPECIFIED\x10\x00\x12$\n\x1f\x45RROR_CODE_MISSING_BEARER_TOKEN\x10\xe9\x07\x12\x1f\n\x1a\x45RROR_CODE_UNAUTHENTICATED\x10\xea\x07\x12!\n\x1c\x45RROR_CODE_MISSING_TENANT_ID\x10\xeb\x07\x12 \n\x1b\x45RROR_CODE_INVALID_AUDIENCE\x10\xec\x07\x12\x1e\n\x19\x45RROR_CODE_INVALID_CLAIMS\x10\xed\x07\x12\x1e\n\x19\x45RROR_CODE_INVALID_ISSUER\x10\xee\x07\x12$\n\x1f\x45RROR_CODE_INVALID_BEARER_TOKEN\x10\xef\x07\x12\x1a\n\x15\x45RROR_CODE_VALIDATION\x10\xd0\x0f\x12$\n\x1f\x45RROR_CODE_UNDEFINED_CHILD_TYPE\x10\xd2\x0f\x12$\n\x1f\x45RROR_CODE_UNDEFINED_CHILD_KIND\x10\xd3\x0f\x12,\n\'ERROR_CODE_UNDEFINED_RELATION_REFERENCE\x10\xd6\x0f\x12+\n&ERROR_CODE_NOT_SUPPORTED_RELATION_WALK\x10\xd7\x0f\x12\x32\n-ERROR_CODE_ENTITY_AND_SUBJECT_CANNOT_BE_EQUAL\x10\xd8\x0f\x12 \n\x1b\x45RROR_CODE_DEPTH_NOT_ENOUGH\x10\xd9\x0f\x12\x41\n<ERROR_CODE_RELATION_REFERENCE_NOT_FOUND_IN_ENTITY_REFERENCES\x10\xda\x0f\x12\x41\n<ERROR_CODE_RELATION_REFERENCE_MUST_HAVE_ONE_ENTITY_REFERENCE\x10\xdb\x0f\x12+\n&ERROR_CODE_DUPLICATED_ENTITY_REFERENCE\x10\xdc\x0f\x12-\n(ERROR_CODE_DUPLICATED_RELATION_REFERENCE\x10\xdd\x0f\x12/\n*ERROR_CODE_DUPLICATED_PERMISSION_REFERENCE\x10\xde\x0f\x12\x1c\n\x17\x45RROR_CODE_SCHEMA_PARSE\x10\xdf\x0f\x12\x1e\n\x19\x45RROR_CODE_SCHEMA_COMPILE\x10\xe0\x0f\x12.\n)ERROR_CODE_SUBJECT_RELATION_MUST_BE_EMPTY\x10\xe1\x0f\x12\x30\n+ERROR_CODE_SUBJECT_RELATION_CANNOT_BE_EMPTY\x10\xe2\x0f\x12\x37\n2ERROR_CODE_SCHEMA_MUST_HAVE_USER_ENTITY_DEFINITION\x10\xe3\x0f\x12!\n\x1c\x45RROR_CODE_UNIQUE_CONSTRAINT\x10\xe4\x0f\x12(\n#ERROR_CODE_INVALID_CONTINUOUS_TOKEN\x10\xe5\x0f\x12\x1b\n\x16\x45RROR_CODE_INVALID_KEY\x10\xe6\x0f\x12$\n\x1f\x45RROR_CODE_ENTITY_TYPE_REQUIRED\x10\xe7\x0f\x12\x34\n/ERROR_CODE_NO_ENTITY_REFERENCES_FOUND_IN_SCHEMA\x10\xe8\x0f\x12 \n\x1b\x45RROR_CODE_INVALID_ARGUMENT\x10\xe9\x0f\x12&\n!ERROR_CODE_INVALID_RULE_REFERENCE\x10\xea\x0f\x12\"\n\x1d\x45RROR_CODE_NOT_SUPPORTED_WALK\x10\xeb\x0f\x12 \n\x1b\x45RROR_CODE_MISSING_ARGUMENT\x10\xec\x0f\x12\x1d\n\x18\x45RROR_CODE_ALREADY_EXIST\x10\xed\x0f\x12+\n&ERROR_CODE_MAX_DATA_PER_WRITE_EXCEEDED\x10\xee\x0f\x12\x19\n\x14\x45RROR_CODE_NOT_FOUND\x10\xa0\x1f\x12%\n ERROR_CODE_ENTITY_TYPE_NOT_FOUND\x10\xa1\x1f\x12$\n\x1f\x45RROR_CODE_PERMISSION_NOT_FOUND\x10\xa2\x1f\x12 \n\x1b\x45RROR_CODE_SCHEMA_NOT_FOUND\x10\xa3\x1f\x12&\n!ERROR_CODE_SUBJECT_TYPE_NOT_FOUND\x10\xa4\x1f\x12+\n&ERROR_CODE_ENTITY_DEFINITION_NOT_FOUND\x10\xa5\x1f\x12/\n*ERROR_CODE_PERMISSION_DEFINITION_NOT_FOUND\x10\xa6\x1f\x12-\n(ERROR_CODE_RELATION_DEFINITION_NOT_FOUND\x10\xa7\x1f\x12 \n\x1b\x45RROR_CODE_RECORD_NOT_FOUND\x10\xa8\x1f\x12 \n\x1b\x45RROR_CODE_TENANT_NOT_FOUND\x10\xa9\x1f\x12.\n)ERROR_CODE_ATTRIBUTE_DEFINITION_NOT_FOUND\x10\xaa\x1f\x12\'\n\"ERROR_CODE_ATTRIBUTE_TYPE_MISMATCH\x10\xab\x1f\x12 \n\x1b\x45RROR_CODE_BUNDLE_NOT_FOUND\x10\xac\x1f\x12)\n$ERROR_CODE_RULE_DEFINITION_NOT_FOUND\x10\xad\x1f\x12*\n%ERROR_CODE_ENTITY_STATEMENT_NOT_FOUND\x10\xae\x1f\x12#\n\x1e\x45RROR_CODE_REFERENCE_NOT_FOUND\x10\xaf\x1f\x12\x18\n\x13\x45RROR_CODE_INTERNAL\x10\x88\'\x12\x19\n\x14\x45RROR_CODE_CANCELLED\x10\x89\'\x12\x1b\n\x16\x45RROR_CODE_SQL_BUILDER\x10\x8a\'\x12\x1f\n\x1a\x45RROR_CODE_CIRCUIT_BREAKER\x10\x8b\'\x12\x19\n\x14\x45RROR_CODE_EXECUTION\x10\x8d\'\x12\x14\n\x0f\x45RROR_CODE_SCAN\x10\x8e\'\x12\x19\n\x14\x45RROR_CODE_MIGRATION\x10\x8f\'\x12!\n\x1c\x45RROR_CODE_TYPE_CONVERSATION\x10\x90\'\x12!\n\x1c\x45RROR_CODE_ERROR_MAX_RETRIES\x10\x91\'\x12\x18\n\x13\x45RROR_CODE_ROLLBACK\x10\x92\'\x12\x39\n4ERROR_CODE_EXCLUSION_REQUIRES_MORE_THAN_ONE_FUNCTION\x10\x93\'\x12\x1f\n\x1a\x45RROR_CODE_NOT_IMPLEMENTED\x10\x94\'\x12\x19\n\x14\x45RROR_CODE_DATASTORE\x10\x95\'\x12&\n!ERROR_CODE_UNKNOWN_STATEMENT_TYPE\x10\x96\'\x12&\n!ERROR_CODE_UNKNOWN_REFERENCE_TYPE\x10\x97\'\x12\x32\n-ERROR_CODE_CANNOT_CONVERT_TO_ENTITY_STATEMENT\x10\x98\'\x12\x34\n/ERROR_CODE_CANNOT_CONVERT_TO_RELATION_STATEMENT\x10\x99\'\x12\x35\n0ERROR_CODE_CANNOT_CONVERT_TO_ATTRIBUTE_STATEMENT\x10\x9a\'B+Z)github.com/Permify/permify/pkg/pb/base/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v1.errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/Permify/permify/pkg/pb/base/v1'
  _globals['_ERRORCODE']._serialized_start=117
  _globals['_ERRORCODE']._serialized_end=2870
  _globals['_ERRORRESPONSE']._serialized_start=33
  _globals['_ERRORRESPONSE']._serialized_end=114
# @@protoc_insertion_point(module_scope)
