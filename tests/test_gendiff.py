from gendiff.generate_diff import generate_diff, choose_format
from tests.fixtures.results import plain_result_meta
from tests.fixtures.results import nested_result_meta
from tests.fixtures.results import stylish_plain_result
from tests.fixtures.results import stylish_nested_result

json_plain_filepath1 = "./tests/fixtures/file1_plain.json"
json_plain_filepath2 = "./tests/fixtures/file2_plain.json"

json_nested_filepath1 = "./tests/fixtures/file1_nested.json"
json_nested_filepath2 = "./tests/fixtures/file2_nested.json"

yaml_plain_filepath1 = "./tests/fixtures/file1_plain.yml"
yaml_plain_filepath2 = "./tests/fixtures/file2_plain.yaml"

yaml_nested_filepath1 = "./tests/fixtures/file1_nested.yaml"
yaml_nested_filepath2 = "./tests/fixtures/file2_nested.yaml"


def test_gendiff_plain_json_meta():
    assert generate_diff(json_plain_filepath1, json_plain_filepath2) == plain_result_meta


def test_gendiff_nested_json_meta():
    assert generate_diff(json_nested_filepath1, json_nested_filepath2) == nested_result_meta


def test_gendiff_plain_yaml_meta():
    assert generate_diff(yaml_plain_filepath1, yaml_plain_filepath2) == plain_result_meta


def test_gendiff_nested_yaml_meta():
    assert generate_diff(yaml_nested_filepath1, yaml_nested_filepath2) == nested_result_meta


def test_plain_stylish_json():
    assert choose_format(generate_diff(json_plain_filepath1,
                                       json_plain_filepath2), "stylish") == stylish_plain_result


def test_nested_stylish_json():
    assert choose_format(generate_diff(json_nested_filepath1,
                                       json_nested_filepath2), "stylish") == stylish_nested_result
