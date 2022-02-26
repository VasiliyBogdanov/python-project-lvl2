from gendiff.generate_diff import generate_diff, choose_format
from tests.fixtures.results import *

flat_json_filepath1 = "./tests/fixtures/file1_flat.json"
flat_json_filepath2 = "./tests/fixtures/file2_flat.json"

nested_json_filepath1 = "./tests/fixtures/file1_nested.json"
nested_json_filepath2 = "./tests/fixtures/file2_nested.json"

flat_yaml_filepath1 = "./tests/fixtures/file1_flat.yaml"
flat_yaml_filepath2 = "./tests/fixtures/file2_flat.yaml"

nested_yaml_filepath1 = "./tests/fixtures/file1_nested.yaml"
nested_yaml_filepath2 = "./tests/fixtures/file2_nested.yaml"


def test_gendiff_flat_json_meta():
    assert generate_diff(flat_json_filepath1, flat_json_filepath2) == flat_result_meta


def test_gendiff_nested_json_meta():
    assert generate_diff(nested_json_filepath1, nested_json_filepath2) == nested_result_meta


def test_gendiff_flat_yaml_meta():
    assert generate_diff(flat_yaml_filepath1, flat_yaml_filepath2) == flat_result_meta


def test_gendiff_nested_yaml_meta():
    assert generate_diff(nested_yaml_filepath1, nested_yaml_filepath2) == nested_result_meta


def test_flat_stylish_json():
    assert choose_format(generate_diff(flat_json_filepath1,
                                       flat_json_filepath2), "stylish") == stylish_flat_result


def test_nested_stylish_json():
    assert choose_format(generate_diff(nested_json_filepath1,
                                       nested_json_filepath2), "stylish") == stylish_nested_result


def test_flat_plain_json():
    assert choose_format(generate_diff(flat_json_filepath1,
                                       flat_json_filepath2), "plain") == plain_flat_result


def test_nested_plain_json():
    assert choose_format(generate_diff(nested_json_filepath1,
                                       nested_json_filepath2), "plain") == plain_nested_result
