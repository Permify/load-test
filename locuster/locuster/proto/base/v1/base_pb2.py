# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/v1/base.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api.expr.v1alpha1 import checked_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_checked__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62\x61se/v1/base.proto\x12\x07\x62\x61se.v1\x1a&google/api/expr/v1alpha1/checked.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\x92\x01\n\x07\x43ontext\x12&\n\x06tuples\x18\x01 \x03(\x0b\x32\x0e.base.v1.TupleR\x06tuples\x12\x32\n\nattributes\x18\x02 \x03(\x0b\x32\x12.base.v1.AttributeR\nattributes\x12+\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructR\x04\x64\x61ta\"{\n\x05\x43hild\x12-\n\x04leaf\x18\x01 \x01(\x0b\x32\r.base.v1.LeafB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x04leaf\x12\x36\n\x07rewrite\x18\x02 \x01(\x0b\x32\x10.base.v1.RewriteB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x07rewriteB\x0b\n\x04type\x12\x03\xf8\x42\x01\"\xbb\x02\n\x04Leaf\x12P\n\x11\x63omputed_user_set\x18\x01 \x01(\x0b\x32\x18.base.v1.ComputedUserSetB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x0f\x63omputedUserSet\x12N\n\x11tuple_to_user_set\x18\x02 \x01(\x0b\x32\x17.base.v1.TupleToUserSetB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x0etupleToUserSet\x12U\n\x12\x63omputed_attribute\x18\x03 \x01(\x0b\x32\x1a.base.v1.ComputedAttributeB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x11\x63omputedAttribute\x12-\n\x04\x63\x61ll\x18\x04 \x01(\x0b\x32\r.base.v1.CallB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00R\x04\x63\x61llB\x0b\n\x04type\x12\x03\xf8\x42\x01\"\xf0\x01\n\x07Rewrite\x12G\n\x11rewrite_operation\x18\x01 \x01(\x0e\x32\x1a.base.v1.Rewrite.OperationR\x10rewriteOperation\x12*\n\x08\x63hildren\x18\x02 \x03(\x0b\x32\x0e.base.v1.ChildR\x08\x63hildren\"p\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fOPERATION_UNION\x10\x01\x12\x1a\n\x16OPERATION_INTERSECTION\x10\x02\x12\x17\n\x13OPERATION_EXCLUSION\x10\x03\"\x8d\x05\n\x10SchemaDefinition\x12_\n\x12\x65ntity_definitions\x18\x01 \x03(\x0b\x32\x30.base.v1.SchemaDefinition.EntityDefinitionsEntryR\x11\x65ntityDefinitions\x12Y\n\x10rule_definitions\x18\x02 \x03(\x0b\x32..base.v1.SchemaDefinition.RuleDefinitionsEntryR\x0fruleDefinitions\x12I\n\nreferences\x18\x03 \x03(\x0b\x32).base.v1.SchemaDefinition.ReferencesEntryR\nreferences\x1a_\n\x16\x45ntityDefinitionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b\x32\x19.base.v1.EntityDefinitionR\x05value:\x02\x38\x01\x1a[\n\x14RuleDefinitionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x17.base.v1.RuleDefinitionR\x05value:\x02\x38\x01\x1a\x62\n\x0fReferencesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x39\n\x05value\x18\x02 \x01(\x0e\x32#.base.v1.SchemaDefinition.ReferenceR\x05value:\x02\x38\x01\"P\n\tReference\x12\x19\n\x15REFERENCE_UNSPECIFIED\x10\x00\x12\x14\n\x10REFERENCE_ENTITY\x10\x01\x12\x12\n\x0eREFERENCE_RULE\x10\x02\"\xdc\x06\n\x10\x45ntityDefinition\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\x12\x46\n\trelations\x18\x02 \x03(\x0b\x32(.base.v1.EntityDefinition.RelationsEntryR\trelations\x12L\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.base.v1.EntityDefinition.PermissionsEntryR\x0bpermissions\x12I\n\nattributes\x18\x04 \x03(\x0b\x32).base.v1.EntityDefinition.AttributesEntryR\nattributes\x12I\n\nreferences\x18\x05 \x03(\x0b\x32).base.v1.EntityDefinition.ReferencesEntryR\nreferences\x1aY\n\x0eRelationsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.base.v1.RelationDefinitionR\x05value:\x02\x38\x01\x1a]\n\x10PermissionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.base.v1.PermissionDefinitionR\x05value:\x02\x38\x01\x1a[\n\x0f\x41ttributesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32\x1c.base.v1.AttributeDefinitionR\x05value:\x02\x38\x01\x1a\x62\n\x0fReferencesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x39\n\x05value\x18\x02 \x01(\x0e\x32#.base.v1.EntityDefinition.ReferenceR\x05value:\x02\x38\x01\"q\n\tReference\x12\x19\n\x15REFERENCE_UNSPECIFIED\x10\x00\x12\x16\n\x12REFERENCE_RELATION\x10\x01\x12\x18\n\x14REFERENCE_PERMISSION\x10\x02\x12\x17\n\x13REFERENCE_ATTRIBUTE\x10\x03\"\xa3\x02\n\x0eRuleDefinition\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\x12\x44\n\targuments\x18\x02 \x03(\x0b\x32&.base.v1.RuleDefinition.ArgumentsEntryR\targuments\x12\x45\n\nexpression\x18\x03 \x01(\x0b\x32%.google.api.expr.v1alpha1.CheckedExprR\nexpression\x1aT\n\x0e\x41rgumentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0e\x32\x16.base.v1.AttributeTypeR\x05value:\x02\x38\x01\"q\n\x13\x41ttributeDefinition\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x16.base.v1.AttributeTypeR\x04type\"\x91\x01\n\x12RelationDefinition\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\x12K\n\x13relation_references\x18\x02 \x03(\x0b\x32\x1a.base.v1.RelationReferenceR\x12relationReferences\"l\n\x14PermissionDefinition\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\x12$\n\x05\x63hild\x18\x02 \x01(\x0b\x32\x0e.base.v1.ChildR\x05\x63hild\"~\n\x11RelationReference\x12.\n\x04type\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04type\x12\x39\n\x08relation\x18\x02 \x01(\tB\x1d\xfa\x42\x1ar\x18(@2\x11^[a-zA-Z_]{1,64}$\xd0\x01\x01R\x08relation\"\xa9\x01\n\x08\x41rgument\x12K\n\x12\x63omputed_attribute\x18\x01 \x01(\x0b\x32\x1a.base.v1.ComputedAttributeH\x00R\x11\x63omputedAttribute\x12H\n\x11\x63ontext_attribute\x18\x02 \x01(\x0b\x32\x19.base.v1.ContextAttributeH\x00R\x10\x63ontextAttributeB\x06\n\x04type\"T\n\x04\x43\x61ll\x12\x1b\n\trule_name\x18\x01 \x01(\tR\x08ruleName\x12/\n\targuments\x18\x02 \x03(\x0b\x32\x11.base.v1.ArgumentR\targuments\"C\n\x11\x43omputedAttribute\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\"B\n\x10\x43ontextAttribute\x12.\n\x04name\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04name\"I\n\x0f\x43omputedUserSet\x12\x36\n\x08relation\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x08relation\"u\n\x0eTupleToUserSet\x12-\n\x08tupleSet\x18\x01 \x01(\x0b\x32\x11.base.v1.TupleSetR\x08tupleSet\x12\x34\n\x08\x63omputed\x18\x02 \x01(\x0b\x32\x18.base.v1.ComputedUserSetR\x08\x63omputed\"B\n\x08TupleSet\x12\x36\n\x08relation\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x08relation\"\xa8\x01\n\x05Tuple\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x0f.base.v1.EntityB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06\x65ntity\x12\x36\n\x08relation\x18\x02 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x08relation\x12\x34\n\x07subject\x18\x03 \x01(\x0b\x32\x10.base.v1.SubjectB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\"\x88\x01\n\tAttribute\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x0f.base.v1.EntityB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06\x65ntity\x12\x1c\n\tattribute\x18\x02 \x01(\tR\tattribute\x12*\n\x05value\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value\"0\n\x06Tuples\x12&\n\x06tuples\x18\x01 \x03(\x0b\x32\x0e.base.v1.TupleR\x06tuples\"@\n\nAttributes\x12\x32\n\nattributes\x18\x01 \x03(\x0b\x32\x12.base.v1.AttributeR\nattributes\"u\n\x06\x45ntity\x12.\n\x04type\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04type\x12;\n\x02id\x18\x02 \x01(\tB+\xfa\x42(r&(\x80\x01\x32!^([a-zA-Z0-9_\\-@\\.:+]{1,128}|\\*)$R\x02id\"~\n\x11\x45ntityAndRelation\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x0f.base.v1.EntityB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06\x65ntity\x12\x36\n\x08relation\x18\x02 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x08relation\"\xb1\x01\n\x07Subject\x12.\n\x04type\x18\x01 \x01(\tB\x1a\xfa\x42\x17r\x15(@2\x11^[a-zA-Z_]{1,64}$R\x04type\x12;\n\x02id\x18\x02 \x01(\tB+\xfa\x42(r&(\x80\x01\x32!^([a-zA-Z0-9_\\-@\\.:+]{1,128}|\\*)$R\x02id\x12\x39\n\x08relation\x18\x03 \x01(\tB\x1d\xfa\x42\x1ar\x18(@2\x11^[a-zA-Z_]{1,64}$\xd0\x01\x01R\x08relation\"`\n\x0f\x41ttributeFilter\x12-\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x15.base.v1.EntityFilterR\x06\x65ntity\x12\x1e\n\nattributes\x18\x02 \x03(\tR\nattributes\"\xa9\x01\n\x0bTupleFilter\x12-\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x15.base.v1.EntityFilterR\x06\x65ntity\x12\x39\n\x08relation\x18\x02 \x01(\tB\x1d\xfa\x42\x1ar\x18(@2\x11^[a-zA-Z_]{1,64}$\xd0\x01\x01R\x08relation\x12\x30\n\x07subject\x18\x03 \x01(\x0b\x32\x16.base.v1.SubjectFilterR\x07subject\"4\n\x0c\x45ntityFilter\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x10\n\x03ids\x18\x02 \x03(\tR\x03ids\"p\n\rSubjectFilter\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x10\n\x03ids\x18\x02 \x03(\tR\x03ids\x12\x39\n\x08relation\x18\x03 \x01(\tB\x1d\xfa\x42\x1ar\x18(@2\x11^[a-zA-Z_]{1,64}$\xd0\x01\x01R\x08relation\"\xf0\x01\n\x0e\x45xpandTreeNode\x12?\n\toperation\x18\x01 \x01(\x0e\x32!.base.v1.ExpandTreeNode.OperationR\toperation\x12+\n\x08\x63hildren\x18\x02 \x03(\x0b\x32\x0f.base.v1.ExpandR\x08\x63hildren\"p\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fOPERATION_UNION\x10\x01\x12\x1a\n\x16OPERATION_INTERSECTION\x10\x02\x12\x17\n\x13OPERATION_EXCLUSION\x10\x03\"\xe8\x01\n\x06\x45xpand\x12\'\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x0f.base.v1.EntityR\x06\x65ntity\x12\x1e\n\npermission\x18\x02 \x01(\tR\npermission\x12/\n\targuments\x18\x03 \x03(\x0b\x32\x11.base.v1.ArgumentR\targuments\x12\x31\n\x06\x65xpand\x18\x04 \x01(\x0b\x32\x17.base.v1.ExpandTreeNodeH\x00R\x06\x65xpand\x12)\n\x04leaf\x18\x05 \x01(\x0b\x32\x13.base.v1.ExpandLeafH\x00R\x04leafB\x06\n\x04node\"\xa3\x01\n\nExpandLeaf\x12/\n\x08subjects\x18\x01 \x01(\x0b\x32\x11.base.v1.SubjectsH\x00R\x08subjects\x12)\n\x06values\x18\x02 \x01(\x0b\x32\x0f.base.v1.ValuesH\x00R\x06values\x12,\n\x05value\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x05valueB\x0b\n\x04type\x12\x03\xf8\x42\x01\"\x8e\x01\n\x06Values\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32\x1b.base.v1.Values.ValuesEntryR\x06values\x1aO\n\x0bValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value:\x02\x38\x01\"8\n\x08Subjects\x12,\n\x08subjects\x18\x01 \x03(\x0b\x32\x10.base.v1.SubjectR\x08subjects\"h\n\x06Tenant\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12:\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreated_at\"f\n\x0b\x44\x61taChanges\x12\x1e\n\nsnap_token\x18\x01 \x01(\tR\nsnap_token\x12\x37\n\x0c\x64\x61ta_changes\x18\x02 \x03(\x0b\x32\x13.base.v1.DataChangeR\x0c\x64\x61ta_changes\"\x86\x02\n\nDataChange\x12;\n\toperation\x18\x01 \x01(\x0e\x32\x1d.base.v1.DataChange.OperationR\toperation\x12&\n\x05tuple\x18\x02 \x01(\x0b\x32\x0e.base.v1.TupleH\x00R\x05tuple\x12\x32\n\tattribute\x18\x03 \x01(\x0b\x32\x12.base.v1.AttributeH\x00R\tattribute\"R\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x14\n\x10OPERATION_CREATE\x10\x01\x12\x14\n\x10OPERATION_DELETE\x10\x02\x42\x0b\n\x04type\x12\x03\xf8\x42\x01\"!\n\x0bStringValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\"\"\n\x0cIntegerValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x05R\x04\x64\x61ta\"!\n\x0b\x44oubleValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x01R\x04\x64\x61ta\"\"\n\x0c\x42ooleanValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x08R\x04\x64\x61ta\"&\n\x10StringArrayValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x03(\tR\x04\x64\x61ta\"\'\n\x11IntegerArrayValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x03(\x05R\x04\x64\x61ta\"&\n\x10\x44oubleArrayValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x03(\x01R\x04\x64\x61ta\"\'\n\x11\x42ooleanArrayValue\x12\x12\n\x04\x64\x61ta\x18\x01 \x03(\x08R\x04\x64\x61ta\"r\n\nDataBundle\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\targuments\x18\x02 \x03(\tR\targuments\x12\x32\n\noperations\x18\x03 \x03(\x0b\x32\x12.base.v1.OperationR\noperations\"\xcb\x01\n\tOperation\x12\x30\n\x13relationships_write\x18\x01 \x03(\tR\x13relationships_write\x12\x32\n\x14relationships_delete\x18\x02 \x03(\tR\x14relationships_delete\x12*\n\x10\x61ttributes_write\x18\x03 \x03(\tR\x10\x61ttributes_write\x12,\n\x11\x61ttributes_delete\x18\x04 \x03(\tR\x11\x61ttributes_delete\"P\n\x08Partials\x12\x14\n\x05write\x18\x01 \x03(\tR\x05write\x12\x16\n\x06\x64\x65lete\x18\x02 \x03(\tR\x06\x64\x65lete\x12\x16\n\x06update\x18\x03 \x03(\tR\x06update*^\n\x0b\x43heckResult\x12\x1c\n\x18\x43HECK_RESULT_UNSPECIFIED\x10\x00\x12\x18\n\x14\x43HECK_RESULT_ALLOWED\x10\x01\x12\x17\n\x13\x43HECK_RESULT_DENIED\x10\x02*\xa3\x02\n\rAttributeType\x12\x1e\n\x1a\x41TTRIBUTE_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x41TTRIBUTE_TYPE_BOOLEAN\x10\x01\x12 \n\x1c\x41TTRIBUTE_TYPE_BOOLEAN_ARRAY\x10\x02\x12\x19\n\x15\x41TTRIBUTE_TYPE_STRING\x10\x03\x12\x1f\n\x1b\x41TTRIBUTE_TYPE_STRING_ARRAY\x10\x04\x12\x1a\n\x16\x41TTRIBUTE_TYPE_INTEGER\x10\x05\x12 \n\x1c\x41TTRIBUTE_TYPE_INTEGER_ARRAY\x10\x06\x12\x19\n\x15\x41TTRIBUTE_TYPE_DOUBLE\x10\x07\x12\x1f\n\x1b\x41TTRIBUTE_TYPE_DOUBLE_ARRAY\x10\x08\x42+Z)github.com/Permify/permify/pkg/pb/base/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.v1.base_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/Permify/permify/pkg/pb/base/v1'
  _globals['_CHILD'].oneofs_by_name['type']._loaded_options = None
  _globals['_CHILD'].oneofs_by_name['type']._serialized_options = b'\370B\001'
  _globals['_CHILD'].fields_by_name['leaf']._loaded_options = None
  _globals['_CHILD'].fields_by_name['leaf']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHILD'].fields_by_name['rewrite']._loaded_options = None
  _globals['_CHILD'].fields_by_name['rewrite']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LEAF'].oneofs_by_name['type']._loaded_options = None
  _globals['_LEAF'].oneofs_by_name['type']._serialized_options = b'\370B\001'
  _globals['_LEAF'].fields_by_name['computed_user_set']._loaded_options = None
  _globals['_LEAF'].fields_by_name['computed_user_set']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LEAF'].fields_by_name['tuple_to_user_set']._loaded_options = None
  _globals['_LEAF'].fields_by_name['tuple_to_user_set']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LEAF'].fields_by_name['computed_attribute']._loaded_options = None
  _globals['_LEAF'].fields_by_name['computed_attribute']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LEAF'].fields_by_name['call']._loaded_options = None
  _globals['_LEAF'].fields_by_name['call']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_SCHEMADEFINITION_ENTITYDEFINITIONSENTRY']._loaded_options = None
  _globals['_SCHEMADEFINITION_ENTITYDEFINITIONSENTRY']._serialized_options = b'8\001'
  _globals['_SCHEMADEFINITION_RULEDEFINITIONSENTRY']._loaded_options = None
  _globals['_SCHEMADEFINITION_RULEDEFINITIONSENTRY']._serialized_options = b'8\001'
  _globals['_SCHEMADEFINITION_REFERENCESENTRY']._loaded_options = None
  _globals['_SCHEMADEFINITION_REFERENCESENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYDEFINITION_RELATIONSENTRY']._loaded_options = None
  _globals['_ENTITYDEFINITION_RELATIONSENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYDEFINITION_PERMISSIONSENTRY']._loaded_options = None
  _globals['_ENTITYDEFINITION_PERMISSIONSENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYDEFINITION_ATTRIBUTESENTRY']._loaded_options = None
  _globals['_ENTITYDEFINITION_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYDEFINITION_REFERENCESENTRY']._loaded_options = None
  _globals['_ENTITYDEFINITION_REFERENCESENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYDEFINITION'].fields_by_name['name']._loaded_options = None
  _globals['_ENTITYDEFINITION'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_RULEDEFINITION_ARGUMENTSENTRY']._loaded_options = None
  _globals['_RULEDEFINITION_ARGUMENTSENTRY']._serialized_options = b'8\001'
  _globals['_RULEDEFINITION'].fields_by_name['name']._loaded_options = None
  _globals['_RULEDEFINITION'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_ATTRIBUTEDEFINITION'].fields_by_name['name']._loaded_options = None
  _globals['_ATTRIBUTEDEFINITION'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_RELATIONDEFINITION'].fields_by_name['name']._loaded_options = None
  _globals['_RELATIONDEFINITION'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_PERMISSIONDEFINITION'].fields_by_name['name']._loaded_options = None
  _globals['_PERMISSIONDEFINITION'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_RELATIONREFERENCE'].fields_by_name['type']._loaded_options = None
  _globals['_RELATIONREFERENCE'].fields_by_name['type']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_RELATIONREFERENCE'].fields_by_name['relation']._loaded_options = None
  _globals['_RELATIONREFERENCE'].fields_by_name['relation']._serialized_options = b'\372B\032r\030(@2\021^[a-zA-Z_]{1,64}$\320\001\001'
  _globals['_COMPUTEDATTRIBUTE'].fields_by_name['name']._loaded_options = None
  _globals['_COMPUTEDATTRIBUTE'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_CONTEXTATTRIBUTE'].fields_by_name['name']._loaded_options = None
  _globals['_CONTEXTATTRIBUTE'].fields_by_name['name']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_COMPUTEDUSERSET'].fields_by_name['relation']._loaded_options = None
  _globals['_COMPUTEDUSERSET'].fields_by_name['relation']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_TUPLESET'].fields_by_name['relation']._loaded_options = None
  _globals['_TUPLESET'].fields_by_name['relation']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_TUPLE'].fields_by_name['entity']._loaded_options = None
  _globals['_TUPLE'].fields_by_name['entity']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_TUPLE'].fields_by_name['relation']._loaded_options = None
  _globals['_TUPLE'].fields_by_name['relation']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_TUPLE'].fields_by_name['subject']._loaded_options = None
  _globals['_TUPLE'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_ATTRIBUTE'].fields_by_name['entity']._loaded_options = None
  _globals['_ATTRIBUTE'].fields_by_name['entity']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_ENTITY'].fields_by_name['type']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['type']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_ENTITY'].fields_by_name['id']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['id']._serialized_options = b'\372B(r&(\200\0012!^([a-zA-Z0-9_\\-@\\.:+]{1,128}|\\*)$'
  _globals['_ENTITYANDRELATION'].fields_by_name['entity']._loaded_options = None
  _globals['_ENTITYANDRELATION'].fields_by_name['entity']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_ENTITYANDRELATION'].fields_by_name['relation']._loaded_options = None
  _globals['_ENTITYANDRELATION'].fields_by_name['relation']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_SUBJECT'].fields_by_name['type']._loaded_options = None
  _globals['_SUBJECT'].fields_by_name['type']._serialized_options = b'\372B\027r\025(@2\021^[a-zA-Z_]{1,64}$'
  _globals['_SUBJECT'].fields_by_name['id']._loaded_options = None
  _globals['_SUBJECT'].fields_by_name['id']._serialized_options = b'\372B(r&(\200\0012!^([a-zA-Z0-9_\\-@\\.:+]{1,128}|\\*)$'
  _globals['_SUBJECT'].fields_by_name['relation']._loaded_options = None
  _globals['_SUBJECT'].fields_by_name['relation']._serialized_options = b'\372B\032r\030(@2\021^[a-zA-Z_]{1,64}$\320\001\001'
  _globals['_TUPLEFILTER'].fields_by_name['relation']._loaded_options = None
  _globals['_TUPLEFILTER'].fields_by_name['relation']._serialized_options = b'\372B\032r\030(@2\021^[a-zA-Z_]{1,64}$\320\001\001'
  _globals['_SUBJECTFILTER'].fields_by_name['relation']._loaded_options = None
  _globals['_SUBJECTFILTER'].fields_by_name['relation']._serialized_options = b'\372B\032r\030(@2\021^[a-zA-Z_]{1,64}$\320\001\001'
  _globals['_EXPANDLEAF'].oneofs_by_name['type']._loaded_options = None
  _globals['_EXPANDLEAF'].oneofs_by_name['type']._serialized_options = b'\370B\001'
  _globals['_VALUES_VALUESENTRY']._loaded_options = None
  _globals['_VALUES_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_DATACHANGE'].oneofs_by_name['type']._loaded_options = None
  _globals['_DATACHANGE'].oneofs_by_name['type']._serialized_options = b'\370B\001'
  _globals['_CHECKRESULT']._serialized_start=7313
  _globals['_CHECKRESULT']._serialized_end=7407
  _globals['_ATTRIBUTETYPE']._serialized_start=7410
  _globals['_ATTRIBUTETYPE']._serialized_end=7701
  _globals['_CONTEXT']._serialized_start=187
  _globals['_CONTEXT']._serialized_end=333
  _globals['_CHILD']._serialized_start=335
  _globals['_CHILD']._serialized_end=458
  _globals['_LEAF']._serialized_start=461
  _globals['_LEAF']._serialized_end=776
  _globals['_REWRITE']._serialized_start=779
  _globals['_REWRITE']._serialized_end=1019
  _globals['_REWRITE_OPERATION']._serialized_start=907
  _globals['_REWRITE_OPERATION']._serialized_end=1019
  _globals['_SCHEMADEFINITION']._serialized_start=1022
  _globals['_SCHEMADEFINITION']._serialized_end=1675
  _globals['_SCHEMADEFINITION_ENTITYDEFINITIONSENTRY']._serialized_start=1305
  _globals['_SCHEMADEFINITION_ENTITYDEFINITIONSENTRY']._serialized_end=1400
  _globals['_SCHEMADEFINITION_RULEDEFINITIONSENTRY']._serialized_start=1402
  _globals['_SCHEMADEFINITION_RULEDEFINITIONSENTRY']._serialized_end=1493
  _globals['_SCHEMADEFINITION_REFERENCESENTRY']._serialized_start=1495
  _globals['_SCHEMADEFINITION_REFERENCESENTRY']._serialized_end=1593
  _globals['_SCHEMADEFINITION_REFERENCE']._serialized_start=1595
  _globals['_SCHEMADEFINITION_REFERENCE']._serialized_end=1675
  _globals['_ENTITYDEFINITION']._serialized_start=1678
  _globals['_ENTITYDEFINITION']._serialized_end=2538
  _globals['_ENTITYDEFINITION_RELATIONSENTRY']._serialized_start=2046
  _globals['_ENTITYDEFINITION_RELATIONSENTRY']._serialized_end=2135
  _globals['_ENTITYDEFINITION_PERMISSIONSENTRY']._serialized_start=2137
  _globals['_ENTITYDEFINITION_PERMISSIONSENTRY']._serialized_end=2230
  _globals['_ENTITYDEFINITION_ATTRIBUTESENTRY']._serialized_start=2232
  _globals['_ENTITYDEFINITION_ATTRIBUTESENTRY']._serialized_end=2323
  _globals['_ENTITYDEFINITION_REFERENCESENTRY']._serialized_start=2325
  _globals['_ENTITYDEFINITION_REFERENCESENTRY']._serialized_end=2423
  _globals['_ENTITYDEFINITION_REFERENCE']._serialized_start=2425
  _globals['_ENTITYDEFINITION_REFERENCE']._serialized_end=2538
  _globals['_RULEDEFINITION']._serialized_start=2541
  _globals['_RULEDEFINITION']._serialized_end=2832
  _globals['_RULEDEFINITION_ARGUMENTSENTRY']._serialized_start=2748
  _globals['_RULEDEFINITION_ARGUMENTSENTRY']._serialized_end=2832
  _globals['_ATTRIBUTEDEFINITION']._serialized_start=2834
  _globals['_ATTRIBUTEDEFINITION']._serialized_end=2947
  _globals['_RELATIONDEFINITION']._serialized_start=2950
  _globals['_RELATIONDEFINITION']._serialized_end=3095
  _globals['_PERMISSIONDEFINITION']._serialized_start=3097
  _globals['_PERMISSIONDEFINITION']._serialized_end=3205
  _globals['_RELATIONREFERENCE']._serialized_start=3207
  _globals['_RELATIONREFERENCE']._serialized_end=3333
  _globals['_ARGUMENT']._serialized_start=3336
  _globals['_ARGUMENT']._serialized_end=3505
  _globals['_CALL']._serialized_start=3507
  _globals['_CALL']._serialized_end=3591
  _globals['_COMPUTEDATTRIBUTE']._serialized_start=3593
  _globals['_COMPUTEDATTRIBUTE']._serialized_end=3660
  _globals['_CONTEXTATTRIBUTE']._serialized_start=3662
  _globals['_CONTEXTATTRIBUTE']._serialized_end=3728
  _globals['_COMPUTEDUSERSET']._serialized_start=3730
  _globals['_COMPUTEDUSERSET']._serialized_end=3803
  _globals['_TUPLETOUSERSET']._serialized_start=3805
  _globals['_TUPLETOUSERSET']._serialized_end=3922
  _globals['_TUPLESET']._serialized_start=3924
  _globals['_TUPLESET']._serialized_end=3990
  _globals['_TUPLE']._serialized_start=3993
  _globals['_TUPLE']._serialized_end=4161
  _globals['_ATTRIBUTE']._serialized_start=4164
  _globals['_ATTRIBUTE']._serialized_end=4300
  _globals['_TUPLES']._serialized_start=4302
  _globals['_TUPLES']._serialized_end=4350
  _globals['_ATTRIBUTES']._serialized_start=4352
  _globals['_ATTRIBUTES']._serialized_end=4416
  _globals['_ENTITY']._serialized_start=4418
  _globals['_ENTITY']._serialized_end=4535
  _globals['_ENTITYANDRELATION']._serialized_start=4537
  _globals['_ENTITYANDRELATION']._serialized_end=4663
  _globals['_SUBJECT']._serialized_start=4666
  _globals['_SUBJECT']._serialized_end=4843
  _globals['_ATTRIBUTEFILTER']._serialized_start=4845
  _globals['_ATTRIBUTEFILTER']._serialized_end=4941
  _globals['_TUPLEFILTER']._serialized_start=4944
  _globals['_TUPLEFILTER']._serialized_end=5113
  _globals['_ENTITYFILTER']._serialized_start=5115
  _globals['_ENTITYFILTER']._serialized_end=5167
  _globals['_SUBJECTFILTER']._serialized_start=5169
  _globals['_SUBJECTFILTER']._serialized_end=5281
  _globals['_EXPANDTREENODE']._serialized_start=5284
  _globals['_EXPANDTREENODE']._serialized_end=5524
  _globals['_EXPANDTREENODE_OPERATION']._serialized_start=907
  _globals['_EXPANDTREENODE_OPERATION']._serialized_end=1019
  _globals['_EXPAND']._serialized_start=5527
  _globals['_EXPAND']._serialized_end=5759
  _globals['_EXPANDLEAF']._serialized_start=5762
  _globals['_EXPANDLEAF']._serialized_end=5925
  _globals['_VALUES']._serialized_start=5928
  _globals['_VALUES']._serialized_end=6070
  _globals['_VALUES_VALUESENTRY']._serialized_start=5991
  _globals['_VALUES_VALUESENTRY']._serialized_end=6070
  _globals['_SUBJECTS']._serialized_start=6072
  _globals['_SUBJECTS']._serialized_end=6128
  _globals['_TENANT']._serialized_start=6130
  _globals['_TENANT']._serialized_end=6234
  _globals['_DATACHANGES']._serialized_start=6236
  _globals['_DATACHANGES']._serialized_end=6338
  _globals['_DATACHANGE']._serialized_start=6341
  _globals['_DATACHANGE']._serialized_end=6603
  _globals['_DATACHANGE_OPERATION']._serialized_start=6508
  _globals['_DATACHANGE_OPERATION']._serialized_end=6590
  _globals['_STRINGVALUE']._serialized_start=6605
  _globals['_STRINGVALUE']._serialized_end=6638
  _globals['_INTEGERVALUE']._serialized_start=6640
  _globals['_INTEGERVALUE']._serialized_end=6674
  _globals['_DOUBLEVALUE']._serialized_start=6676
  _globals['_DOUBLEVALUE']._serialized_end=6709
  _globals['_BOOLEANVALUE']._serialized_start=6711
  _globals['_BOOLEANVALUE']._serialized_end=6745
  _globals['_STRINGARRAYVALUE']._serialized_start=6747
  _globals['_STRINGARRAYVALUE']._serialized_end=6785
  _globals['_INTEGERARRAYVALUE']._serialized_start=6787
  _globals['_INTEGERARRAYVALUE']._serialized_end=6826
  _globals['_DOUBLEARRAYVALUE']._serialized_start=6828
  _globals['_DOUBLEARRAYVALUE']._serialized_end=6866
  _globals['_BOOLEANARRAYVALUE']._serialized_start=6868
  _globals['_BOOLEANARRAYVALUE']._serialized_end=6907
  _globals['_DATABUNDLE']._serialized_start=6909
  _globals['_DATABUNDLE']._serialized_end=7023
  _globals['_OPERATION']._serialized_start=7026
  _globals['_OPERATION']._serialized_end=7229
  _globals['_PARTIALS']._serialized_start=7231
  _globals['_PARTIALS']._serialized_end=7311
# @@protoc_insertion_point(module_scope)
