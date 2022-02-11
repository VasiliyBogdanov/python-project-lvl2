import argparse
import json


def cli_arg_parser():
    parser = argparse.ArgumentParser(description="Generate diff")

    # Positional arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # Optional arguments
    parser.add_argument("-f", "--format",
                        help="set format of output",
                        default="plain json")

    args = parser.parse_args()
    filepath1, filepath2 = args.first_file, args.second_file
    format_ = args.format
    print(generate_diff(filepath1, filepath2, format_))


def _true_false_to_string(item):
    if item is True:
        return "true"
    elif item is False:
        return "false"
    else:
        return item


def _plain_json_diff(filepath_a: str, filepath_b: str) -> str:
    with open(filepath_a) as f1, open(filepath_b) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
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


def generate_diff(filepath_a: str, filepath_b: str, format_: str = "plain json") -> str:
    if format_ == "plain json":
        return _plain_json_diff(filepath_a, filepath_b)
