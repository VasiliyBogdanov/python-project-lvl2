import json
import yaml
from gendiff.parser.arg_parser import FILE_FORMAT_JSON
from gendiff.parser.arg_parser import FILE_FORMAT_YAML


def load_file(filepath, file_format):
    if file_format == FILE_FORMAT_JSON:
        with open(filepath, mode="r") as f:
            file = json.load(f)
    elif file_format == FILE_FORMAT_YAML:
        with open(filepath, mode="r") as f:
            file = yaml.safe_load(f)

    return file
