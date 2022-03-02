import os

FILE_FORMAT_JSON = "json"
FILE_FORMAT_YAML = "yaml"


def check_file_format(filepath):
    file_format = os.path.splitext(filepath)[-1]

    if file_format == ".json":
        return FILE_FORMAT_JSON
    elif file_format in (".yml", ".yaml"):
        return FILE_FORMAT_YAML
    else:
        raise Exception("Incorrect file type")
