import json

import yaml


def parse_file_format(text, file_format):

    if file_format == ".json":
        return parse_json(text)
    elif file_format in (".yml", ".yaml"):
        return parse_yaml(text)
    else:
        raise Exception("Incorrect file type")


def parse_json(text: str):
    data = json.loads(text)
    return data


def parse_yaml(text: str):
    data = yaml.safe_load(text)
    return data
