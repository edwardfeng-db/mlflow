import re
import sys

from string_utils import camel_to_snake, snake_to_pascal

INDENT = " " * 4
INDENT2 = INDENT * 2
SCHEMA_EXTENSION = "mlflow/server/graphql/graphql_schema_extensions.py"


def get_package_name(method_descriptor):
    return method_descriptor.containing_service.file.package


# Get method name in snake case. Result is package name followed by the method name.
def get_method_name(method_descriptor):
    return get_package_name(method_descriptor) + "_" + camel_to_snake(method_descriptor.name)


def get_descriptor_full_pascal_name(field_descriptor):
    return snake_to_pascal(field_descriptor.full_name.replace(".", "_"))


def method_descriptor_to_generated_pb2_file_name(method_descriptor):
    return re.sub(r"\.proto", "_pb2", method_descriptor.containing_service.file.name)


def debugLog(log):
    print(log, file=sys.stderr)
