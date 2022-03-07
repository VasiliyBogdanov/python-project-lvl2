from gendiff.generate_diff import build_diff, generate_diff
from gendiff.parsers.file_parser import parse_file_format
from gendiff.parsers.file_parser import read_file
from tests.fixtures.meta_tree_results import flat_result_meta
from tests.fixtures.meta_tree_results import nested_result_meta


def open_result_file(filepath):
    with open(filepath) as f:
        result = f.read()
    return result


def prepare_file(filepath):
    text_data, extension = read_file(filepath)
    file = parse_file_format(text_data, extension)

    return file


# Initial data filepaths
flat_json_filepath1 = "./tests/fixtures/file1_flat.json"
flat_json_filepath2 = "./tests/fixtures/file2_flat.json"

nested_json_filepath1 = "./tests/fixtures/file1_nested.json"
nested_json_filepath2 = "./tests/fixtures/file2_nested.json"

flat_yaml_filepath1 = "./tests/fixtures/file1_flat.yaml"
flat_yaml_filepath2 = "./tests/fixtures/file2_flat.yaml"

nested_yaml_filepath1 = "./tests/fixtures/file1_nested.yaml"
nested_yaml_filepath2 = "./tests/fixtures/file2_nested.yaml"

# Results filepaths
stylish_flat_result_filepath = "./tests/fixtures/gendiff_results/stylish_flat_result.txt"
stylish_nested_result_filepath = "./tests/fixtures/gendiff_results/stylish_nested_result.txt"

plain_flat_result_filepath = "./tests/fixtures/gendiff_results/plain_flat_result.txt"
plain_nested_result_filepath = "./tests/fixtures/gendiff_results/plain_nested_result.txt"

json_flat_result_filepath = "./tests/fixtures/gendiff_results/json_flat_result.txt"
json_nested_result_filepath = "./tests/fixtures/gendiff_results/json_nested_result.txt"


# Test result of "build_diff" function
def test_build_meta_tree_flat_json():
    assert build_diff(prepare_file(flat_json_filepath1),
                      prepare_file(flat_json_filepath2)) == flat_result_meta


def test_build_meta_tree_nested_json():
    assert build_diff(prepare_file(nested_json_filepath1),
                      prepare_file(nested_json_filepath2)) == nested_result_meta


def test_build_meta_tre_flat_yaml():
    assert build_diff(prepare_file(flat_yaml_filepath1),
                      prepare_file(flat_yaml_filepath2)) == flat_result_meta


def test_build_meta_tre_nested_yaml():
    assert build_diff(prepare_file(nested_yaml_filepath1),
                      prepare_file(nested_yaml_filepath2)) == nested_result_meta


# Test result of "generate_diff" function
def test_flat_stylish_json():
    assert generate_diff(flat_json_filepath1,
                         flat_json_filepath2, "stylish") == open_result_file(stylish_flat_result_filepath)


def test_nested_stylish_json():
    assert generate_diff(nested_json_filepath1,
                         nested_json_filepath2, "stylish") == open_result_file(stylish_nested_result_filepath)


def test_flat_plain_json():
    assert generate_diff(flat_json_filepath1,
                         flat_json_filepath2, "plain") == open_result_file(plain_flat_result_filepath)


def test_nested_plain_json():
    assert generate_diff(nested_json_filepath1,
                         nested_json_filepath2, "plain") == open_result_file(plain_nested_result_filepath)


def test_flat_json():
    assert generate_diff(flat_json_filepath1,
                         flat_json_filepath2, "json") == open_result_file(json_flat_result_filepath)


def test_nested_json():
    assert generate_diff(nested_json_filepath1,
                         nested_json_filepath2, "json") == open_result_file(json_nested_result_filepath)
