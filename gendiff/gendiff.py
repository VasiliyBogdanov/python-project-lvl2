import json
import os
import yaml


def _true_false_to_string(item):
    if item is True:
        return "true"
    elif item is False:
        return "false"
    else:
        return item


def _prepare_file(filepath: str):
    file_format = os.path.splitext(filepath)[-1]
    if file_format == ".json":
        with open(filepath) as f:
            file = json.load(f)
    elif file_format == ".yml" or file_format == ".yaml":
        with open(filepath) as f:
            file = yaml.safe_load(f)
    return file


def _create_diff(filepath_a: str, filepath_b: str, format_: str) -> str:
    file1, file2 = _prepare_file(filepath_a), _prepare_file(filepath_b)
    file1 = {k: _true_false_to_string(v) for k, v in file1.items()}
    file2 = {k: _true_false_to_string(v) for k, v in file2.items()}

    # Modified elements before changes
    diff_a_to_b = dict(set(file1.items()).difference(set(file2.items())))
    # Modified elements after changes
    diff_b_to_a = dict(set(file2.items()).difference(set(file1.items())))

    aggregator = file1.copy()
    aggregator.update(file2)
    aggregator = sorted((k, v) for k, v in aggregator.items())

    output = ""
    for key, value in aggregator:
        if key not in diff_a_to_b and key not in diff_b_to_a:
            output += f"    {key}: {value}\n"
        elif key in diff_a_to_b and key not in diff_b_to_a:
            output += f"  - {key}: {diff_a_to_b[key]}\n"
        elif key in diff_b_to_a and key not in diff_a_to_b:
            output += f"  + {key}: {diff_b_to_a[key]}\n"
        else:
            output += f"  - {key}: {diff_a_to_b[key]}\n"
            output += f"  + {key}: {diff_b_to_a[key]}\n"
    output = "{\n" + output + "}"
    return output


def generate_diff(filepath_a: str, filepath_b: str, format_: str) -> str:
    return _create_diff(filepath_a, filepath_b, format_)
