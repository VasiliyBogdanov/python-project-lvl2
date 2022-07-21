from gendiff.parsers.file_parser import parse_file_format
from gendiff.parsers.file_parser import read_file


def open_result_file(filepath):
    with open(filepath) as f:
        result = f.read()
    return result


def prepare_file(filepath):
    text_data, extension = read_file(filepath)
    file = parse_file_format(text_data, extension)

    return file


# Initial data filepaths
FLAT_JSON_FILEPATH1 = "./tests/fixtures/file1_flat.json"
FLAT_JSON_FILEPATH2 = "./tests/fixtures/file2_flat.json"

NESTED_JSON_FILEPATH1 = "./tests/fixtures/file1_nested.json"
NESTED_JSON_FILEPATH2 = "./tests/fixtures/file2_nested.json"

FLAT_YAML_FILEPATH1 = "./tests/fixtures/file1_flat.yaml"
FLAT_YAML_FILEPATH2 = "./tests/fixtures/file2_flat.yaml"

NESTED_YAML_FILEPATH1 = "./tests/fixtures/file1_nested.yaml"
NESTED_YAML_FILEPATH2 = "./tests/fixtures/file2_nested.yaml"

# Results filepaths
STYLISH_FLAT_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/stylish_flat_result.txt"
STYLISH_NESTED_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/stylish_nested_result.txt"

PLAIN_FLAT_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/plain_flat_result.txt"
PLAIN_NESTED_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/plain_nested_result.txt"

JSON_FLAT_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/json_flat_result.txt"
JSON_NESTED_RESULT_FILEPATH = "./tests/fixtures/gendiff_results/json_nested_result.txt"
